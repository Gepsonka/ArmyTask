from dataclasses import field
from django import forms
from .models import ManufacturerNamesModel, CarTypesModel

    
CHOICES = (
    ('gas', 'Gas'),
    ('diesel', 'Diesel'),
    ('lpg', 'LPG gas')
)

class CarAddFavouritesForm(forms.Form):
    year = forms.IntegerField(min_value=1880)
    color = forms.CharField(max_length=20)
    fuel = forms.ChoiceField(choices=CHOICES)

class CarAddTypeForm(forms.ModelForm):
    manufacturer = forms.ModelChoiceField(queryset=ManufacturerNamesModel.objects.all())
    name = forms.CharField(max_length=255)

    class Meta:
        model = CarTypesModel
        fields = ['manufacturer', 'name']

class CarRequestManufacturerForm(forms.Form):
    manufacturer_name = forms.CharField(max_length=255)

    