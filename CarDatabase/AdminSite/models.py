from django.db import models

# Create your models here.

class CarNewManufacturerRequestsModel(models.Model):
    name = models.CharField(unique=True, max_length=255)

    def __str__(self) -> str:
        return f'{self.name} request'