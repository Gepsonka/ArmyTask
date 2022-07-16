from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    unsuccessful_attempts = models.SmallIntegerField(default=0)
    requested_delete = models.BooleanField(default=False)
    requested_unlock = models.BooleanField(default=False)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    
