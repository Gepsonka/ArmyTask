from email.utils import parseaddr
from django.shortcuts import render, redirect
from CustomUser.models import CustomUser
from django.contrib import messages
from .forms import AdminUserCreationForm
from CustomUser.decorators import admin_required
from django.contrib.auth.decorators import login_required



# Create your views here.

@admin_required('home')
def users_page_view(request):
    # Return the lis of all users to the template
    all_users = CustomUser.objects.all()
    return render(request, 'AdminSite/templates/users.html', {'all_users': all_users})

@admin_required('home')
def user_creation_view(request):
    '''
    View to create users by the admins. 
    By default an admin can select any password she/he likes (validators are not applied).
    The view checks if there are any users with the same username or password,
    if there is not any create a new user with the given credentials, else send error.
    '''    
    if request.method=='POST':
        form = AdminUserCreationForm(request.POST)
        

        if form.is_valid():
            # Check if user with the same username or email exists
            try:
                # If user does not exists thee xpression below throws
                # an exeption so the user can be created
                user_by_username = CustomUser.objects.get(username=form.cleaned_data.get('username'))
            except:
                user_by_username = None

            if user_by_username is not None:
                messages.error(request, 'User with that username is already exists.')
                return redirect('admin-users')

            try:
                user_by_email = CustomUser.objects.get(email=form.cleaned_data.get('email'))
            except:
                user_by_email = None

            if user_by_email is not None:
                messages.error(request, 'User with that email is already exists.')
                return redirect('admin-users')

            CustomUser.objects.create_user(
                username=form.cleaned_data.get('username'),
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data.get('last_name'),
                email=form.cleaned_data.get('email'),
                password=form.cleaned_data.get('password'),
                is_active=form.cleaned_data.get('is_active'),
                is_staff=form.cleaned_data.get('is_staff'),
                is_superuser=form.cleaned_data.get('is_superuser')
            )

            messages.success(request, 'User created sucessfully.')
            return redirect('admin-user-creation')
    else:
        form = AdminUserCreationForm()

    return render(request, 'AdminSite/templates/admin_user_creation.html', {'form':form})

@admin_required('home')
def user_delete_page_view(request):
    delete_request_users = CustomUser.objects.filter(requested_delete=True)
    return render(request, 'AdminSite/templates/admin_user_delete.html', {'delete_request_users': delete_request_users})

@admin_required('home')
def user_delete_view(request, id):
    if request.method=='POST':
        try:
            CustomUser.objects.get(id=id).delete()
            messages.success(request, 'User was successfully deleted')

            # Have to redirect back to the admin-users page bc otherwise
            # it would not refresh the list
            return redirect('admin-users')
        except:
            messages.error(request, "Error! User does not exists!")
    return redirect('admin-users')

@admin_required('home')
def user_delete_all_view(request):
    if request.method=='POST':
        CustomUser.objects.filter(requested_delete=True).delete()
        messages.success(request, 'All requested deletion was successful.')
    return redirect('admin-user-unlock')

@admin_required('home')
def user_unlock_page_view(request):
    unlock_request_users = CustomUser.objects.filter(requested_unlock=True)
    return render(request, 'AdminSite/templates/admin_user_unlock.html', {'unlock_request_users': unlock_request_users})


@admin_required('home')
def user_unlock_view(request, id):
    if request.method=='POST':
        try:
            # Activating the user
            user = CustomUser.objects.get(id=id)
            user.unsuccessful_attempts=0
            user.is_active=True
            user.requested_unlock=False
            user.save()
            messages.success(request, 'Account was successfully unlocked.')
        except:
            messages.error(request, "Error! User does not exists!")
    
    return redirect('admin-user-unlock')

@admin_required('home')
def user_unlock_all_view(request):
    if request.method=='POST':
        CustomUser.objects.filter(requested_unlock=True).update(unsuccessful_attempts=0, is_active=True, requested_unlock=False)
        messages.success(request, 'All account were successfully unlocked.')
    return redirect('admin-user-unlock')

@admin_required('home')
def make_admin(request, id):
    if request.method=='POST':
        try:
            user = CustomUser.objects.get(id=id)
            user.is_superuser = True
            user.save()
            username = user.username
            messages.success(request, 'Successfully added admin privileges to ' + username)
        except:
            messages.error(request, "Error! User does not exists!")
    return redirect('admin-users')


@admin_required('home')
def revoke_admin(request, id):
    if request.method=='POST':
        try:
            user = CustomUser.objects.get(id=id)
            user.is_superuser = False
            user.save()
            username = user.username
            messages.success(request, 'Successfully revoked admin privileges from ' + username)
        except:
            messages.error(request, "Error! User does not exists!")
    return redirect('admin-users')