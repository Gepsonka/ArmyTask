from django.db import models
from CustomUser.models import CustomUser

# Create your models here.
class AccountActivationRequestModel(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + "'s request for activation"
    
    