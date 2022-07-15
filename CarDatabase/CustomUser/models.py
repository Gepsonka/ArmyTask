from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    unsuccessful_attempts = models.SmallIntegerField(default=0)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    
class AccountDeleteRequestModel(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + "'s request for delete"