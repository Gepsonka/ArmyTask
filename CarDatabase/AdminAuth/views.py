from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages

# Create your views here.


def admin_login_view(request):
    '''Admin login view. Admins can only use this view to log in.'''

    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method=='POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            # Making sure only admins can log in here
            if not user.is_superuser and not user.is_staff:
                messages.error(request, f'User with the given credentials does not exists.')
                return render(request, 'AdminAuth/templates/admin_login.html', {'form': form})

            login(request, user)
            return redirect('admin-users')

        else:
            form = AuthenticationForm()
            messages.error(request, f'User with the given credentials does not exists.')
    else:
        form = AuthenticationForm()

    return render(request, 'AdminAuth/templates/admin_login.html', {'form': form})
        


    