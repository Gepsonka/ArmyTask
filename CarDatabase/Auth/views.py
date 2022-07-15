from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from CustomUser.forms import UserRegisterForm
from CustomUser.models import CustomUser
from Auth.models import UserActivationRequestModel

# Create your views here.


def registration_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
    else:
        form = UserRegisterForm()
        
    return render(request, 'Auth/templates/register.html', {'form': form})


def login_view(request):
    # if the user is already authenticated redirect to the home page
    if request.user.is_authenticated:
        return redirect('home')
        
    
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticating user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # admins cannot log in here
            if user.is_superuser or user.is_staff:
                messages.warning(request, f'Admins cannot log in here.')
                return render(request, 'Auth/templates/login.html', {'form': form})
            
            
            if user.unsuccessful_attempts >= 5:
                pass
            
            # Update unsuccessfull attempts to 0 after successful login
            user.unsuccessful_attempts = 0
            user.save()
            
            login(request, user)
            return redirect('home')
        
        else:
            user = CustomUser.objects.get(username = username)
            
            if user.is_superuser or user.is_staff:
                messages.warning(request, f'Admins cannot log in here.')
                return render(request, 'Auth/templates/login.html', {'form': form})
            
            if user is not None:
                # If the user can be identified by username after an unsuccessful login
                # increase the number of unsuccessful logins of the user and send a message
                user.unsuccessful_attempts += 1
                user.save()
                
                # If the user failed to log in more than
                # 5 times we do no display the remaining attempts.
                if 5 - user.unsuccessful_attempts > 0:
                    messages.warning(request, f'You have {5 - user.unsuccessful_attempts} attempts remaining')
                
                # If the user has exceeded the maximum attempts of login,
                # lock the acccount then return a message to the frontend.
                if user.unsuccessful_attempts >= 5:
                    if user.is_active:
                        user.is_active = False
                        user.save()
                    messages.error(request, "Your account has been locked. Request to unlock.")
                    return render(request, 'Auth/templates/login.html', {'form': form})

            else:
                # If the user cannot be identified then just return a message
                messages.error(request, f'Unsuccessful login')
        
    else:
        form = AuthenticationForm()
        
    return render(request, 'Auth/templates/login.html', {'form': form})
    
def request_account_retrieve_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        
        prop_user = CustomUser.objects.get(username = username)
        if prop_user is not None:
            prop_user
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_superuser or user.is_staff:
                messages.warning(request, "Admins cannot retreive accounts.")
                return render(request, 'Auth/templates/request_acc_activation.html', {'form':form})
            
            # If the account is active do nothing and inform the user
            if user.is_active:
                messages.info(request, "Account is active.")
                return render(request, 'Auth/templates/request_acc_activation.html', {'form':form})
            else:
                user_request = UserActivationRequestModel.objects.get(user=user)
                # If the current user does not have a request, create one
                # else inform the user that there is already an activation process is ongoing.
                if user_request == None:
                    # Creating new request for the user to activate the account
                    UserActivationRequestModel.objects.create(user=user).save()
                    messages.success(request, 'You have successfully requested account activation. Wait for the activation from the admins.')
                    return render(request, 'Auth/templates/request_acc_activation.html', {'form':form})
                else:
                    messages.info(request, 'Your account is already waiting for activation!')
                    return render(request, 'Auth/templates/request_acc_activation.html', {'form':form})
        else:
            messages.error(request, "User with the given credentials does not exists.")
            return render(request, 'Auth/templates/request_acc_activation.html', {'form':form})
            
    else:
        form = AuthenticationForm()
        
    return render(request, 'Auth/templates/request_acc_activation.html', {'form':form})