from django import forms
from CustomUser.models import CustomUser
from CarData.models import ManufacturerNamesModel
from django.utils.translation import gettext as _



# class AdminUserCreationForm(forms.Form):
#     '''Makes the admins be able to create new users from the admin site with this form.'''
#     username = forms.CharField(label='Username', max_length=150)
#     first_name = forms.CharField(label='First name', max_length=255)
#     last_name = forms.CharField(label='Last name', max_length=255)
#     email = forms.EmailField(label='Email')
#     password = forms.CharField(widget=forms.PasswordInput(), label='Password')
#     is_active = forms.BooleanField(required=False, label='Is active?')
#     is_superuser = forms.BooleanField(required=False, label='Is superuser?')

class AdminUserCreationForm(forms.ModelForm):
    '''Form to create user from the admin site'''
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'is_active', 'is_superuser']

    def save(self, commit: bool = True):
        '''Has to be rewritten otherwise it would not hash the password'''
        instance = super().save(commit)

        # Do the passwd hashing
        instance.set_password(self.cleaned_data.get('password'))

        if commit:
            instance.save()

        return instance


class AdminUserUpdateForm(forms.Form):
    '''Makes the admins be able to create new users from the admin site with this form.'''
    username = forms.CharField(label='Username', max_length=150, required=False)
    first_name = forms.CharField(label='First name', max_length=255, required=False)
    last_name = forms.CharField(label='Last name', max_length=255, required=False)
    email = forms.EmailField(label='Email', required=False)
    password = forms.CharField(widget=forms.PasswordInput(), label='Password', required=False)
    is_active = forms.BooleanField(required=False, label='Is active?')
    is_superuser = forms.BooleanField(required=False, label='Is superuser?')

    def __init__(self, *args, **kwargs):
        '''Had to override __init__ to add user attribute and to pass it from view'''
        self.user = kwargs.pop('user', None) # using pop for security reasons
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()

        if self.user.username != cleaned_data.get('username') and CustomUser.objects.filter(username=cleaned_data.get('username')).exists():
            raise forms.ValidationError({'username': ['User with that username already exists', ]})

        if self.user.email != cleaned_data.get('email') and CustomUser.objects.filter(email=cleaned_data.get('email')).exists():
            raise forms.ValidationError({'email': ['User with that email already exists', ]})

class AdminManufacturerCreationForm(forms.ModelForm):
    class Meta:
        model = ManufacturerNamesModel
        fields = ['name']
        
    def clean(self):
        cleaned_data = super().clean()
        
        if ManufacturerNamesModel.objects.filter(name=cleaned_data.get('name')).exists():
            raise forms.ValidationError({'name': ['Manufacturer already exists',]})