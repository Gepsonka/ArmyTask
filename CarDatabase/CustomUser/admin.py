from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, AccountDeleteRequestModel
from .forms import UserRegisterForm


# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = UserRegisterForm
#    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username"]
    


admin.site.register(CustomUser, CustomUserAdmin)
