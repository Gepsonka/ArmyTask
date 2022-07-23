from cmath import exp
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from CustomUser.forms import UserRegisterForm
from CustomUser.models import CustomUser
from .froms import AccountRetrieveForm
from CustomUser.decorators import not_logged_in_required

# Create your views here.


@not_logged_in_required('home')
def registration_view(request):
    '''User registration is processed here'''

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
    else:
        form = UserRegisterForm()
        
    return render(request, 'Auth/templates/register.html', {'form': form})

@not_logged_in_required('home')
def login_view(request):
    '''Login view for normal users'''
    # We only process data if the request method is POST
    # else we just render the page
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticating user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # admins cannot log in here
            if user.is_superuser:
                messages.warning(request, f'Admins cannot log in here.')
                return render(request, 'Auth/templates/login.html', {'form': form})
            
            # If the user has reaches the max unsuccessful login attempts
            # check if he/she has already asked for unlock and send a messsage
            # according to the check
            if not user.is_active:                
                # If the user already sent a request we inform him/her about it
                if user.requested_unlock:
                    messages.error(request, "You have requested to unlock your account. Wait till the admins unlock it")
                    return render(request, 'Auth/templates/login.html', {'form': form})
                    
                else:
                    messages.error(request, "Your account has been locked. Request to unlock.")
                    return render(request, 'Auth/templates/login.html', {'form': form})
            # Update unsuccessfull attempts to 0 after successful login
            user.unsuccessful_attempts = 0
            user.save()
            
            login(request, user)
            return redirect('home')
        
        else:
            # If the user with the given username does not exists
            # make user None
            # Required because if the CustomUser.objects.get(username = username) query
            # does not find the object it raises an error
            try:
                user = CustomUser.objects.get(username = username)
            except:
                user = None
            
            
            if user is not None:
                # If the user can be identified by username after an unsuccessful login
                # increase the number of unsuccessful logins of the user and send a message
                user.unsuccessful_attempts += 1
                user.save()
                
                # If the user failed to log in more than
                # 5 times we do not display the remaining attempts.
                if 5 - user.unsuccessful_attempts > 0:
                    messages.warning(request, f'You have {5 - user.unsuccessful_attempts} attempts remaining')
                
                # If the user has exceeded the maximum attempts of login,
                # lock the acccount then return a message to the frontend.
                if user.unsuccessful_attempts >= 5:
                    if user.is_active:
                        user.is_active = False
                        user.save()
                    
                    # If the user already sent a request/did not send a request we inform him/her about it
                    if not user.requested_unlock:
                        messages.error(request, "Your account has been locked. Request to unlock.")
                        return render(request, 'Auth/templates/login.html', {'form': form})
                    else:
                        messages.error(request, "You have requested to unlock your account. Wait till the admins unlock it")
                        return render(request, 'Auth/templates/login.html', {'form': form})

            else:
                # If the user cannot be identified by usermame then just return a message
                messages.error(request, f'Unsuccessful login')
        
    else:
        form = AuthenticationForm()
        
    return render(request, 'Auth/templates/login.html', {'form': form})


@not_logged_in_required('home')
def request_account_retrieve_view(request):
    '''
    The user can ask for account unlock after reaching the max amount of
    failed login attempts.
    '''
    
    if request.method == 'POST':
        form = AccountRetrieveForm(request.POST)
        username = request.POST['username']
        
        try:
            current_user = CustomUser.objects.get(username=username)
        except:
            current_user = None
        
        
        if current_user is not None:
            # Since admin's account cannot be locked, they cannot retrieve accounts
            if current_user.is_superuser or current_user.is_staff:
                messages.warning(request, "Admins cannot retreive accounts.")
                return render(request, 'Auth/templates/request_acc_activation.html', {'form':form})
            
            # If the account is active do nothing and inform the user
            if current_user.is_active:
                messages.info(request, "Account is active.")
                return render(request, 'Auth/templates/request_acc_activation.html', {'form':form})
            else:
                # If the current user does not have a request, create one
                # else inform the user that there is already an activation process is ongoing.
                if not current_user.requested_unlock:
                    # Creating new request for the user to activate the account
                    current_user.requested_unlock = True
                    current_user.save()
                    messages.success(request, 'You have successfully requested account activation. Wait for the activation from the admins.')
                    return render(request, 'Auth/templates/request_acc_activation.html', {'form':form})
                else:
                    messages.info(request, 'Your account is already waiting for activation!')
                    return render(request, 'Auth/templates/request_acc_activation.html', {'form':form})
        else:
            messages.error(request, "User with the given credentials does not exists.")
            return render(request, 'Auth/templates/request_acc_activation.html', {'form':form})
            
    else:
        form = AccountRetrieveForm()
        
    return render(request, 'Auth/templates/request_acc_activation.html', {'form':form})