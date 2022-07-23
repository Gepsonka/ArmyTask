from dataclasses import field, fields
from django import forms
from .models import *
from AdminSite.models import CarNewManufacturerRequestsModel, CarNewManufacturerRequestsDeleteModel
from django.utils.translation import gettext as _

    
CHOICES = (
    ('Gas', 'Gas'),
    ('Diesel', 'Diesel'),
    ('LPG gas', 'LPG gas'),
    ('Electric', 'Electric'),
    ('Hybrid', 'Hybrid'),
)

class CarAddFavouritesForm(forms.Form):
    '''
    This form is used when the user adds an already existing
    car. This way the manufacturer and the model is known
    the user only need to specify the color, year and fuel type
    '''

    year = forms.IntegerField(min_value=1880)
    color = forms.CharField(max_length=50)
    fuel = forms.ChoiceField(choices=CHOICES)
    


class CarAddFavouritesSeparatelyForm(forms.ModelForm):
    '''
    Using this the user has to specify not only the year,color and fuel type
    but the manufacturer and the model too.
    If a model is exists, just add to favourites, else create new
    model with the selected manufacturer and make that favourite.
    '''
    manufacturer = forms.ModelChoiceField(queryset=ManufacturerNamesModel.objects.all())
    car_type = forms.CharField(max_length=255)
    year = forms.IntegerField(min_value=1880)
    fuel = forms.ChoiceField(choices=CHOICES)
    
    class Meta:
        model = FavouriteCarsModel
        fields = ['manufacturer', 'year', 'color', 'fuel']
        
    def __init__(self, *args, **kwargs):
        '''Had to override __init__ to add user attribute and to pass it from view'''

        self.user = kwargs.pop('user', None) # using pop for security reasons
        super().__init__(*args, **kwargs)
    
    def clean(self):
        '''Basic validation of the form'''
        cleaned_data = super().clean()
        
        if not ManufacturerNamesModel.objects.filter(name=cleaned_data.get('manufacturer')).exists():
            raise forms.ValidationError({'manufacturer':['Manufacturer does not exists!',]})
        
        # Do not forget that user, year and car_type are unique together!
        if (FavouriteCarsModel.objects.filter(
                user=self.user,
                year=cleaned_data.get('year'),
                car_type__manufacturer__name=cleaned_data.get('manufacturer')
            ).exists()):
            raise forms.ValidationError(_('Car already between your favourites.'))
                
    def save(self, commit=True):
        '''
        Override of the save() method in order to check if the type already exists,
        if not create new one.
        '''
        instance = super().save(commit=False)
        
        # If the type does not exists create new one and set to the favourite car type
        # else just set the type for the favourite car
        if not CarTypesModel.objects.filter(name=self.cleaned_data.get('car_type')).exists():
            new_type = CarTypesModel.objects.create(
                    manufacturer=ManufacturerNamesModel.objects.filter(name=self.cleaned_data.get('manufacturer')).first(),
                    name=self.cleaned_data.get('car_type')
                )
            instance.car_type = new_type
            new_type.save()
            
        instance.car_type = CarTypesModel.objects.filter(name=self.cleaned_data.get('car_type')).first()
            
        if commit:
            instance.save()
        
        return instance

class CarUpdateFavouriteCarForm(forms.ModelForm):
    '''
    Used for updating favourite cars.
    The user can only update the year, color and fuel type.
    If the user wants to update the manufacturer/model it is easier
    to delete the current car from favourites and create a new favourite car
    '''

    fuel = forms.ChoiceField(choices=CHOICES)
    class Meta:
        model = FavouriteCarsModel
        fields = ['year', 'color', 'fuel']


class CarAddTypeForm(forms.ModelForm):
    '''User can add car model with this form.'''

    manufacturer = forms.ModelChoiceField(queryset=ManufacturerNamesModel.objects.all())
    name = forms.CharField(max_length=255)

    class Meta:
        model = CarTypesModel
        fields = ['manufacturer', 'name']

class CarUploadCarImageForm(forms.ModelForm):
    '''
    User can upload image to his/her favourite car with this form.
    '''
    class Meta:
        model = CarPicturesModel
        fields = ['picture']

class CarRequestManufacturerForm(forms.ModelForm):
    '''Users can request yet non existent manufacturers to be added.'''

    class Meta:
        model = CarNewManufacturerRequestsModel
        fields = ['name']

    def clean(self):
        '''
        Checking if the requested manufacturer is
        already requested or already exists.
        '''
        cleaned_data = super().clean()
        
        if ManufacturerNamesModel.objects.filter(name=cleaned_data.get('name')).exists():
            raise forms.ValidationError({'name':['Manufacturer already exists!',]})

        if CarNewManufacturerRequestsModel.objects.filter(name=cleaned_data.get('name')).exists():
            raise forms.ValidationError({'name':['Manufacturer is already requested!',]})


    
class CarRequestDeleteOfManufacturerForm(forms.ModelForm):
    '''
    Users can request manufacturer delete manufacturers
    for i.e. when a manufacturer is duplicated or if someone accidetally
    added non existent manufacturer.
    '''
    manufacturer = forms.ModelChoiceField(queryset=ManufacturerNamesModel.objects.all())
    class Meta:
        model = CarNewManufacturerRequestsDeleteModel
        fields = ['manufacturer']

    def clean(self):
        '''
        Checking if the requested manufacturer is
        already requested or already exists.
        '''
        cleaned_data = super().clean()

        if CarNewManufacturerRequestsDeleteModel.objects.filter(manufacturer__name=cleaned_data.get('manufacturer')).exists():
            raise forms.ValidationError({'manufacturer':['Delete is already requested!',]})

        if not ManufacturerNamesModel.objects.filter(name=cleaned_data.get('manufacturer')).exists():
            raise forms.ValidationError({'manufacturer':['Manufacturer does not exists!',]})

    