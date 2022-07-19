from dataclasses import field
from django import forms
from CustomUser.models import CustomUser


class AdminUserForm(forms.Form):
    '''Makes the admins be able to create new users from the admin site with this form.'''
    username = forms.CharField(label='Username', max_length=150)
    first_name = forms.CharField(label='First name', max_length=255)
    last_name = forms.CharField(label='Last name', max_length=255)
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')
    is_active = forms.BooleanField(required=False, label='Is active?')
    is_superuser = forms.BooleanField(required=False, label='Is superuser?')

class AdminUserUpdateForm(forms.Form):
    '''Makes the admins be able to create new users from the admin site with this form.'''
    username = forms.CharField(label='Username', max_length=150, required=False)
    first_name = forms.CharField(label='First name', max_length=255, required=False)
    last_name = forms.CharField(label='Last name', max_length=255, required=False)
    email = forms.EmailField(label='Email', required=False)
    password = forms.CharField(widget=forms.PasswordInput(), label='Password', required=False)
    is_active = forms.BooleanField(required=False, label='Is active?')
    is_superuser = forms.BooleanField(required=False, label='Is superuser?')


class AdminManufacturerCreationForm(forms.Form):
    name = forms.CharField(max_length=50, label='Manufacturer name')