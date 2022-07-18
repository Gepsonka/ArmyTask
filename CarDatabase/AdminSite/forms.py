import email
from urllib.robotparser import RequestRate
from django import forms


class AdminUserForm(forms.Form):
    '''Makes the admins be able to create new users from the admin site with this form.'''
    username = forms.CharField(label='Username', max_length=150)
    first_name = forms.CharField(label='First name', max_length=255)
    last_name = forms.CharField(label='Last name', max_length=255)
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')
    is_active = forms.BooleanField(required=False, label='Is active?')
    is_superuser = forms.BooleanField(required=False, label='Is superuser?')

