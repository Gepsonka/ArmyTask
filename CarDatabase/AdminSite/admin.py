from django.contrib import admin
from .models import CarNewManufacturerRequestsModel, CarNewManufacturerRequestsDeleteModel

# Register your models here.
admin.site.register(CarNewManufacturerRequestsModel)
admin.site.register(CarNewManufacturerRequestsDeleteModel)
