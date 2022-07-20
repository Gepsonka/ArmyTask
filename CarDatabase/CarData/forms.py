from dataclasses import field
from django import forms
from .models import ManufacturerNamesModel, CarTypesModel, FavouriteCarsModel
from django.utils.translation import gettext as _

    
CHOICES = (
    ('Gas', 'Gas'),
    ('Diesel', 'Diesel'),
    ('LPG gas', 'LPG gas'),
    ('Electric', 'Electric')
)

class CarAddFavouritesForm(forms.Form):
    year = forms.IntegerField(min_value=1880)
    color = forms.CharField(max_length=50)
    fuel = forms.ChoiceField(choices=CHOICES)
    
class CarAddFavouritesSeparatelyForm(forms.ModelForm):
    manufacturer = forms.ModelChoiceField(queryset=ManufacturerNamesModel.objects.all())
    car_type = forms.CharField(max_length=255)
    year = forms.IntegerField(min_value=1880)
    fuel = forms.ChoiceField(choices=CHOICES)
    
    class Meta:
        model = FavouriteCarsModel
        fields = ['manufacturer', 'year', 'color', 'fuel']
        
    def __init__(self, *args, **kwargs):
       self.user = kwargs.pop('user', None) # using pop for security reasons
       super().__init__(*args, **kwargs)
    
    def clean(self):
        cleaned_data = super().clean()
        
        if not ManufacturerNamesModel.objects.filter(name=cleaned_data.get('manufacturer')).exists():
            raise forms.ValidationError({'manufacturer':['Manufacturer does not exists!',]})
        
        if (FavouriteCarsModel.objects.filter(
                user=self.user,
                year=cleaned_data.get('year'),
                car_type=CarTypesModel.objects.filter(
                            name=cleaned_data.get('car_type'),
                            manufacturer = ManufacturerNamesModel.objects.filter(name=cleaned_data.get('manufacturer')).first()
                        ).first(),
            ).exists()):
            raise forms.ValidationError(_('Car already between your favourites.'))
                
    def save(self, commit=True):
        instance = super().save(commit=False)
        
        # If the type does not exists create new one and set to the favourit car type
        # else just set the type for the favourite car
        if not CarTypesModel.objects.filter(name=self.cleaned_data.get('car_type')).exists():
            new_type = CarTypesModel.objects.create(
                    manufacturer=ManufacturerNamesModel.objects.filter(name=self.cleaned_data.get('manufacturer')).first(),
                    name=self.cleaned_data.get('car_type')
                )
            new_type.save()
            instance.car_type = new_type
        else:
            instance.car_type = CarTypesModel.objects.filter(name=self.cleaned_data.get('car_type')).first()
            
        if commit:
            instance.save()
        
        return instance

class CarAddTypeForm(forms.ModelForm):
    manufacturer = forms.ModelChoiceField(queryset=ManufacturerNamesModel.objects.all())
    name = forms.CharField(max_length=255)

    class Meta:
        model = CarTypesModel
        fields = ['manufacturer', 'name']

class CarRequestManufacturerForm(forms.Form):
    manufacturer_name = forms.CharField(max_length=255)
    
    

    