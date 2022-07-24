from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, MaxLengthValidator
# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=16, validators=[MinLengthValidator(6), MaxLengthValidator(16)], unique=True)
    email = models.EmailField(unique=True)
    unsuccessful_attempts = models.SmallIntegerField(default=0)
    requested_delete = models.BooleanField(default=False)
    requested_unlock = models.BooleanField(default=False)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    
    