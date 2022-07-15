from django.contrib import admin
from .models import AccountActivationRequestModel


# Register your models here.
class AuthAdmin(admin.ModelAdmin):
    pass


admin.site.register(AccountActivationRequestModel, AuthAdmin)