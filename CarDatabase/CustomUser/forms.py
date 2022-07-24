from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MinLengthValidator, MaxLengthValidator


from .models import CustomUser

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(required=True, min_length=6, validators=[MinLengthValidator(6), MaxLengthValidator(16)])
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        
