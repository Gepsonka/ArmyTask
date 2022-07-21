from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import CarPicturesModel, ManufacturerNamesModel, CarTypesModel, FavouriteCarsModel
from AdminSite.models import CarNewManufacturerRequestsModel
from django.contrib import messages
from CustomUser.decorators import not_admin_required


# Create your views here.
def home_view(request):
    return render(request, "CarData/templates/home.html")


@login_required
def car_favourites_view(requests):
    pass

@login_required
def car_base_view(request):
    if request.method == 'POST':
        # If the user tries to filter to the default option in the dropdown
        if not 'manufacturer' in dict(request.POST):
            filtered_car_types = CarTypesModel.objects.all()
            
        else:
            filtered_car_types = CarTypesModel.objects.filter(
                manufacturer__name = request.POST['manufacturer']
            )

    else:
        filtered_car_types = filtered_car_types = CarTypesModel.objects.all()


    manufacturers = ManufacturerNamesModel.objects.all()
    return render(request, 'CarData/templates/car_list_cars.html', {'filtered_car_types':filtered_car_types,
                                                            'manufacturers': manufacturers})  

@login_required
def car_favourite_car_list_view(request):
    manufacturers = ManufacturerNamesModel.objects.all()        

    if request.method == 'POST':
        # If the user tries to filter to the default option in the dropdown return all
        if not 'manufacturer' in dict(request.POST):
            favourite_car_types = FavouriteCarsModel.objects.filter(user=request.user)
            return render(request, 'CarData/templates/car_favourite_cars_list.html', {'favourite_car_types':favourite_car_types,
                                                            'manufacturers': manufacturers})
        
        # Does not work, I dunno why, oh that's why
        favourite_car_types = FavouriteCarsModel.objects.filter(
            user=request.user,
            # Basically saying select those cars which car type's manufacturer's name is equal to request.POST['manufacturer']
            car_type__manufacturer__name=request.POST['manufacturer']
        )    
    else:
        # If the page is being sent to the client side
        favourite_car_types = FavouriteCarsModel.objects.filter(user=request.user)

    return render(request, 'CarData/templates/car_favourite_cars_list.html', {'favourite_car_types':favourite_car_types,
                                                            'manufacturers': manufacturers})  

@login_required
def car_favourite_car_update_page_view(request, pk):
    if not FavouriteCarsModel.objects.filter(pk=pk, user=request.user).exists():
        messages.error(request, 'Car is not between your favourites.')
        return redirect('car-favourite-car-update-page', pk)

    favourite_car = FavouriteCarsModel.objects.filter(pk=pk, user=request.user).first()
    car_images = CarPicturesModel.objects.filter(user_favourite_car = favourite_car)

    if request.method == 'POST':
        form = CarUpdateFavouriteCarForm(request.POST, instance=favourite_car)

        if form.is_valid():
            form.save()

            messages.success(request, 'Favourite car was successfully updated')
            return redirect('car-favourite-car-update-page', pk)
    else:
        update_form = CarUpdateFavouriteCarForm(initial={
            'year': favourite_car.year,
            'color': favourite_car.color,
            'fuel': favourite_car.fuel
        })
        upload_car_image_form = CarUploadCarImageForm()

    return render(request, 'CarData/templates/car_modify_favourite_car.html', 
            {
                'favourite_car': favourite_car,
                'update_form':update_form,
                'upload_car_image_form': upload_car_image_form,
                'car_images': car_images,
            }
        )
    

@login_required
def car_delete_car_from_favourites_view(request,pk):
    if request.method == 'POST':
        if not FavouriteCarsModel.objects.filter(pk=pk, user=request.user).exists():
            messages.error(request, 'Car between your favourites could not found.')
            return redirect('car-favourite-cars-list')
        
        FavouriteCarsModel.objects.filter(pk=pk, user=request.user).delete()
        messages.success(request, 'Car was successfully removed from your favourites.')
        return redirect('car-favourite-cars-list')

@login_required
def car_add_to_favourites_view(request, pk):
    if not CarTypesModel.objects.filter(pk=pk).exists():
        messages.error(request, 'Car type not found')
        return redirect('car-query')
    else:
        car_type = CarTypesModel.objects.filter(pk=pk).first()

    if request.method == 'POST':
        form = CarAddFavouritesForm(request.POST)

        if form.is_valid():
            if FavouriteCarsModel.objects.filter(car_type=car_type, year=form.cleaned_data.get('year')).exists():
                messages.error(request, 'Car is already between your favourites')
                return redirect('car-query')

            FavouriteCarsModel.objects.create(
                car_type=car_type,
                user=request.user,
                year=form.cleaned_data.get('year'),
                color=form.cleaned_data.get('color'),
                fuel=form.cleaned_data.get('fuel')
            ).save()
            
            messages.success(request, 'Car successfully added to favourites.')
            return redirect('car-query')

        else:
            messages.error(request, 'Unkown error occurred!')
            return redirect('car-query')

    else:
        form = CarAddFavouritesForm()

    return render(request, 'CarData/templates/car_add_favourite.html', {'form':form,'car_type':car_type})

@login_required
def car_add_to_favourites_separate_view(request):
    if request.method == 'POST':
        form = CarAddFavouritesSeparatelyForm(request.POST, user=request.user)
        
        if form.is_valid():
            fav_car = form.save(commit=False)
            fav_car.user = request.user
            fav_car.save()
            
            messages.success(request, 'Car was successfully added to your favourites.')
            return redirect('car-favourite-cars-list')
    else:
        form = CarAddFavouritesSeparatelyForm()
        
    return render(request, "CarData/templates/car_add_favourite_separate.html", {'form':form})

@login_required
def create_car_type_view(request):
    '''Creating type which later can be added to favourites or '''
    if request.method == 'POST':
        form = CarAddTypeForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Car type successfully created.')
            return redirect('car-query')

    else:
        form = CarAddTypeForm()

    return render(request, 'CarData/templates/car_create_new_type.html', {'form': form})

@login_required
@not_admin_required('home', 'Admins cannot reach this page ( You have access to the db )')
def create_manufacturer_request_view(request):
    '''
    Creating request for a manufacturer which later can be signed
    by an admin, adding manufacturer to the database permanently (or delete the request).
    '''
    if request.method == 'POST':
        form = CarRequestManufacturerForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully created request!')
            return redirect('car-query')
    
    else:
        form = CarRequestManufacturerForm()

    return render(request, 'CarData/templates/car_new_manufacturer_request.html', {'form':form})

@login_required
@not_admin_required('home', 'Admins cannot reach this page ( You have access to the db )')
def car_create_manufacturer_delete_request_view(request):
    if request.method == 'POST':
        form = CarRequestDeleteOfManufacturerForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, 'Successfully created request!')

    else:
        form = CarRequestDeleteOfManufacturerForm()

    return render(request, 'CarData/templates/car_manufacturer_request_for_delete.html', {'form':form})
    
@login_required
def car_upload_image_view(request, pk):
    '''
    Favourite car image upload view.
    Firt check if the favourite car is truly the user's,
    then upoad.
    pk: FavouriteCarsModel's pk
    '''
    if request.method == 'POST':
        # if the picture is not one of the user's favourite car's
        if not FavouriteCarsModel.objects.filter(pk=pk, user=request.user).exists():
            messages.error(request, 'Could not upload image to the car.')
            return redirect('car-favourite-car-update-page', pk)

        favourite_car = FavouriteCarsModel.objects.filter(pk=pk, user=request.user).first()
        form = CarUploadCarImageForm(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user_favourite_car = favourite_car
            instance.save()

            messages.success(request, 'Image was successfully uploaded!')
    
    return redirect('car-favourite-car-update-page', pk)
            

@login_required
def car_image_delete_view(request, pk):
    '''
    User can delete picture from his/her favourite car.
    pk: CarPicturesModel's pk
    '''
    if request.method == 'POST':
        # if the picture is not one of the user's favourite car's
        if not CarPicturesModel.objects.filter(pk=pk, user_favourite_car__user=request.user).exists():
            messages.error(request, 'Could not upload image to the car.')
            return redirect('car-favourite-cars-list')
            
        picture = CarPicturesModel.objects.filter(pk=pk, user_favourite_car__user=request.user).first()
        fav_car_pk = picture.user_favourite_car.pk
        picture.delete()

        messages.success(request, 'Picture was successfully deleted.')
        return redirect('car-favourite-car-update-page', fav_car_pk)

    return redirect('car-favourite-cars-list')