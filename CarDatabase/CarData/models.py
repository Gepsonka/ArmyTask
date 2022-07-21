from distutils.command.upload import upload
from django.db import models
from CustomUser.models import CustomUser
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date
from PIL import Image

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
    
    class Meta:
        unique_together = ('manufacturer', 'name')

class FavouriteCarsModel(models.Model):
    '''User can select favourite cars from the available models'''
    car_type = models.ForeignKey(CarTypesModel, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    year = models.PositiveIntegerField(validators=[MinValueValidator(1880),MaxValueValidator(date.today().year)])
    color = models.CharField(max_length=50)
    fuel  = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}\'s favourite: {self.car_type.__str__()}'

    class Meta:
        unique_together = ('car_type', 'user', 'year')

class CarPicturesModel(models.Model):
    user_favourite_car = models.ForeignKey(FavouriteCarsModel, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='cars')

    def __str__(self) -> str:
        return f'{self.user_favourite_car.user.first_name} {self.user_favourite_car.user.last_name}\'s picture of {self.user_favourite_car.car_type.__str__()}.'

    def save(self):
        super().save()  # saving image first

        img = Image.open(self.picture.path) # Open image using self
        basewidth = 300

        if img.height > 300 or img.width > 300:
            wpercent = (basewidth / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((basewidth, hsize), Image.ANTIALIAS)
            img.save(self.picture.path)  # saving image at the same path