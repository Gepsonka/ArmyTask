from django.db import models
from CarData.models import ManufacturerNamesModel

# Create your models here.

class CarNewManufacturerRequestsModel(models.Model):
    name = models.CharField(unique=True, max_length=255)

    def __str__(self) -> str:
        return f'{self.name} request'


class CarNewManufacturerRequestsDeleteModel(models.Model):
    manufacturer = models.OneToOneField(ManufacturerNamesModel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.manufacturer.name}\'s request for delete'
