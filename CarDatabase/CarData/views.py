from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CarManufacturerSelectionForm
from .models import ManufacturerNamesModel, CarTypesModel
from django.contrib import messages


# Create your views here.
def home_view(request):
    return render(request, "CarData/templates/home.html")


@login_required
def car_base_view(request):
    
    if request.method == 'POST':
        form = CarManufacturerSelectionForm(request.POST)

        if form.is_valid():
            filtered_car_types = CarTypesModel(
                manufacturer = ManufacturerNamesModel.objects.filter(name=form.cleaned_data.get('manufacturer_select').first())
            )
        
        else:
            filtered_car_types = []
            messages.error(request, 'Unknown error occurred!')
    
    else:
        filtered_car_types = []
        form = CarManufacturerSelectionForm()

    return render(request, 'CarData/templates/car_add_favourite.html', {'form':form, 'filtered_car_types':filtered_car_types})