from django.shortcuts import render
from .froms import UserRegisterForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from User.models import UserLoginUnsuccessfulAttemptsModel

# Create your views here.
def registration_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
    else:
        form = UserRegisterForm()
        
    return render(request, 'Auth/templates/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticating user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            # Update unsuccessfull attempts to 0 after successful login
            UserLoginUnsuccessfulAttemptsModel.objects.filter(user=user).update(unsuccessful_attempts = UserLoginUnsuccessfulAttemptsModel.objects.filter(user=user).unsuccessful_attempts + 1)

        else:
            pass
        
    else:
        form = AuthenticationForm()
        
    return render(request, 'Auth/templates/login.html', {'form': form})
    
    