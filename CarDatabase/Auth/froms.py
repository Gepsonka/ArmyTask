from django import forms
from django.contrib.auth.forms import UserCreationForm
from CustomUser.models import CustomUser


class AccountRetrieveForm(forms.Form):
    '''Used for retrieving user accounts which the admin can accept'''
    
    username = forms.CharField(label="Username", max_length=255)
    