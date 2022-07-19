from django import forms
from .models import ManufacturerNamesModel

    
CHOICES = (
    ('gas', 'Gas'),
    ('diesel', 'Diesel'),
    ('lpg', 'LPG gas')
)

class CarAddFavouritesForm(forms.Form):
    year = forms.IntegerField(min_value=1880)
    color = forms.CharField(max_length=20)
    fuel = forms.ChoiceField(choices=CHOICES)

class CarAddTypeForm(forms.Form):
    car_type = forms.CharField(max_length=255)

class CarRequestManufacturerForm(forms.Form):
    manufacturer_name = forms.CharField(max_length=255)