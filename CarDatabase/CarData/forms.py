from django import forms
from .models import ManufacturerNamesModel


class CarManufacturerSelectionForm(forms.Form):
    manufacturer_select = forms.Select(choices=list([( manufacturer.name, manufacturer.pk ) for manufacturer in ManufacturerNamesModel.objects.all()]))

    
