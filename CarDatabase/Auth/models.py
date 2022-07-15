from django.db import models
from CustomUser.models import CustomUser

# Create your models here.
class UserActivationRequestModel(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    
    