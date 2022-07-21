from sre_constants import SUCCESS
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import (CarAddFavouritesForm, CarRequestManufacturerForm, CarAddTypeForm,
                     CarAddFavouritesSeparatelyForm, CarUpdateFavouriteCarForm,
                      CarUploadCarImageForm)
from .models import ManufacturerNamesModel, CarTypesModel, FavouriteCarsModel
from AdminSite.models import CarNewManufacturerRequestsModel
from django.contrib import messages


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
            manufacturers = ManufacturerNamesModel.objects.all()
            return render(request, 'CarData/templates/car_list_cars.html', {'filtered_car_types':[],
                                                            'manufacturers': manufacturers})
    
        filtered_car_types = CarTypesModel.objects.filter(
            manufacturer = ManufacturerNamesModel.objects.filter(name=request.POST['manufacturer']).first()
        )

    else:
        filtered_car_types = []

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
        return redirect('car-update-favourite-car', pk)

    if request.method == 'POST':
        form = CarUpdateFavouriteCarForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, 'Favourite car successfully updated')
            return redirect('car-update-favourite-car', pk)

    update_form = CarUpdateFavouriteCarForm()
    upload_car_image_form = CarUploadCarImageForm()

    return render(request=)
    

@login_required
def car_favourite_car_update_action_view(request, pk):
    if request.method == 'POST':
        if not FavouriteCarsModel.objects.filter(pk=pk, user=request.user).exists():
            messages.error(request, 'Car is not between your favourites.')
            return redirect('car-update-favourite-car', pk)

        form = CarUpdateFavouriteCarForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, 'Favourite car successfully updated')
            return redirect('car-update-favourite-car', pk)


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
def create_manufacturer_request_view(request):
    if request.method == 'POST':
        form = CarRequestManufacturerForm(request.POST)

        if form.is_valid():
            if (CarNewManufacturerRequestsModel.objects.filter(name=form.cleaned_data.get('manufacturer_name')).exists()
                or ManufacturerNamesModel.objects.filter(name=form.cleaned_data.get('manufacturer_name')).exists()):
                messages.error(request, 'Manufacturer or request already exists.')
                return render(request, 'CarData/templates/car_new_manufacturer_request.html', {'form':form})


            CarNewManufacturerRequestsModel.objects.create(name=form.cleaned_data.get('manufacturer_name')).save()

            messages.success(request, 'Successfully created request!')
            return redirect('car-query')

        else:
            messages.error(request, 'Unknown error occurred')
            
    
    else:
        form = CarRequestManufacturerForm()

    return render(request, 'CarData/templates/car_new_manufacturer_request.html', {'form':form})
    
