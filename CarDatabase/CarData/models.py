from distutils.command.upload import upload
from django.db import models
from CustomUser.models import CustomUser

# Create your models here.

class ManufacturerNamesModel(models.Model):
    '''Representing manufacturer names like BMW, Suzuki, Toyota'''
    name = models.CharField(unique=True, max_length=50)

class CarTypesModel(models.Model):
    '''Representing car models like X5, Swift, Yaris'''
    manufacturer = models.ForeignKey(ManufacturerNamesModel, on_delete=models.CASCADE)
    name = models.CharField(unique=True, max_length=100)

class FavouriteCarsModel(models.Model):
    car_type = models.ForeignKey(CarTypesModel, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    fuel  = models.CharField(max_length=20)

class CarPicturesModel(models.Model):
    user_favourite_car = models.ForeignKey(FavouriteCarsModel, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='cars')
