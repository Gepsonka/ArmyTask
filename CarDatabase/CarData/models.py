from distutils.command.upload import upload
from django.db import models
from CustomUser.models import CustomUser

# Create your models here.

class ManufacturerNamesModel(models.Model):
    '''Representing manufacturer names like BMW, Suzuki, Toyota'''
    name = models.CharField(unique=True, max_length=50)

    def __str__(self) -> str:
        return self.name

class CarTypesModel(models.Model):
    '''Representing car models like X5, Swift, Yaris'''
    manufacturer = models.ForeignKey(ManufacturerNamesModel, on_delete=models.CASCADE)
    name = models.CharField(unique=True, max_length=255)

    def __str__(self) -> str:
        return self.manufacturer.name + ' ' + self.name

class FavouriteCarsModel(models.Model):
    '''User can select favourite cars from the available models'''
    car_type = models.ForeignKey(CarTypesModel, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    fuel  = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}\'s favourite: {self.car_type.__str__()}'

    class Meta:
        unique_together = ('car_type', 'user', 'year')

class CarPicturesModel(models.Model):
    user_favourite_car = models.ForeignKey(FavouriteCarsModel, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='cars')
