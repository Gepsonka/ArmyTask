from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class UserLoginUnsuccessfulAttemptsModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    unsuccessful_attempts = models.SmallIntegerField(default=0)