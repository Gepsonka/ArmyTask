from django import forms
from django.contrib.auth.forms import UserCreationForm




class AccountRetrieveForm(forms.Form):
    username = forms.CharField(label="Username", max_length=255)