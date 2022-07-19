from django.contrib import admin
from .models import (ManufacturerNamesModel, CarTypesModel, 
                FavouriteCarsModel, CarPicturesModel)

# Register your models here.

admin.site.register(ManufacturerNamesModel)
admin.site.register(CarTypesModel)
admin.site.register(FavouriteCarsModel)
admin.site.register(CarPicturesModel)
