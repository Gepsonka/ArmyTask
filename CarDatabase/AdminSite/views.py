from email.utils import parseaddr
from django.shortcuts import render, redirect
from CustomUser.models import CustomUser
from django.contrib import messages
from .forms import AdminUserForm
from CustomUser.decorators import admin_required
from django.contrib.auth.decorators import login_required



# Create your views here.

@admin_required('home')
def users_page_view(request):
    '''
    Page displaying all the users to the admin.
     - If the user's row is blue: the user is admin
     - If the user's row is red: the user requested a delete
     - if the user's row is yellow: the user requested an unlock
    '''
    # Return the lis of all users to the template
    all_users = CustomUser.objects.all()
    return render(request, 'AdminSite/templates/users.html', {'all_users': all_users})

@admin_required('home')
def user_creation_view(request):
    '''
    View to create users by the admins. 
    By default an admin can select any password she/he would like to (validators are not applied).
    The view checks if there are any users with the same username or password,
    if there is not any create a new user with the given credentials, else send error message.
    '''    
    if request.method == 'POST':
        form = AdminUserForm(request.POST)
        
        if form.is_valid():
            # Check if user with the same username or email exists
            try:
                # If the user exists thee expression below throws
                # an exeption so the user can be created
                user_by_username = CustomUser.objects.get(username=form.cleaned_data.get('username'))
                messages.error(request, 'User with that username is already exists.')
                return redirect('admin-users')
            except:
                pass

            try:
                # If the user exists the expression below throws
                # an exeption so a new user can be created
                user_by_email = CustomUser.objects.get(email=form.cleaned_data.get('email'))
                messages.error(request, 'User with that email is already exists.')
                return redirect('admin-users')
            except:
                pass
                

            CustomUser.objects.create_user(
                username=form.cleaned_data.get('username'),
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data.get('last_name'),
                email=form.cleaned_data.get('email'),
                password=form.cleaned_data.get('password'),
                is_active=form.cleaned_data.get('is_active'),
                is_superuser=form.cleaned_data.get('is_superuser')
            )

            messages.success(request, 'User created sucessfully.')
            return redirect('admin-users')
    else:
        form = AdminUserForm()

    return render(request, 'AdminSite/templates/admin_user_creation.html', {'form':form})


@admin_required('home')
def user_update_page_view(request, id):
    try:
        user_update = CustomUser.objects.get(id=id)
    except:
        messages.error(request, 'Error! Could not update account because the account does not exist.')
        return redirect('admin-users')

    if request.method == 'POST':
        form = AdminUserForm(request.POST)

        if form.is_valid():
            user_update.username=form.cleaned_data.get('username'),
            user_update.first_name=form.cleaned_data.get('first_name'),
            user_update.last_name=form.cleaned_data.get('last_name'),
            user_update.email=form.cleaned_data.get('email'),
            user_update.is_active=form.cleaned_data.get('is_active'),
            user_update.is_superuser=form.cleaned_data.get('is_superuser')

            # Updating password (only if not empty)
            if form.cleaned_data.get('password') == '':
                user_update.set_password(form.cleaned_data.get('password'))
            

        messages.success(request, form.cleaned_data.get('username') + 'was successfully updated!')
        return redirect('admin-users')

    else:
        # If the page is requested we display the account's current credentials.
        form = AdminUserForm(initial={
            'username': user_update.username,
            'first_name': user_update.first_name,
            'last_name': user_update.last_name,
            'email': user_update.email,
            'password': '',
            'is_active': user_update.is_active,
            'is_superuser': user_update.is_superuser
        })

    return render(request, 'AdminSite/templates/admin_user_update.html', {'form':form, 'current_user':user_update})



@admin_required('home')
def user_delete_page_view(request):
    '''
    On this page the admins can delete users wether
    clicking on the Delete all: this deletes all the users who
    requested it
    or the X button at the end of each row which deletes one user.
    '''
    delete_request_users = CustomUser.objects.filter(requested_delete=True)
    return render(request, 'AdminSite/templates/admin_user_delete.html', {'delete_request_users': delete_request_users})

@admin_required('home')
def user_delete_view(request, id):
    '''
    Deletes an user by id. If the user does not exists,
    sends back an error message.
    '''
    if request.method == 'POST':
        try:
            CustomUser.objects.get(id=id).delete()
            messages.success(request, 'User was successfully deleted')

            return redirect('admin-users')
        except:
            messages.error(request, "Error! User does not exists!")
    return redirect('admin-users')

@admin_required('home')
def user_delete_all_view(request):
    '''Deletes all the users who requested a delete.'''
    if request.method=='POST':
        CustomUser.objects.filter(requested_delete=True).delete()
        messages.success(request, 'All requested deletion was successful.')
    return redirect('admin-user-delete')

@admin_required('home')
def user_unlock_page_view(request):
    '''
    Displays the users who requested unlock.
    Users can be unlocked with the button at the end of each row, it unlocks one account
    or with the Unlock all button which unlocks all accounts who requested.
    '''
    unlock_request_users = CustomUser.objects.filter(requested_unlock=True)
    return render(request, 'AdminSite/templates/admin_user_unlock.html', {'unlock_request_users': unlock_request_users})


@admin_required('home')
def user_unlock_view(request, id):
    '''Unlocks account by id.'''
    if request.method=='POST':
        try:
            # Activating the user
            user = CustomUser.objects.get(id=id)
            # Checks if the account is actually locked
            # If not do nothing and send back an error message
            if user.unsuccessful_attempts < 5 and user.is_active:
                messages.error(request, 'User is active. No need to unlock.')
                return redirect('admin-user-unlock')
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
    '''Unlocks all accounts who requested an unlock.'''
    if request.method=='POST':
        CustomUser.objects.filter(requested_unlock=True).update(unsuccessful_attempts=0, is_active=True, requested_unlock=False)
        messages.success(request, 'All account were successfully unlocked.')
    return redirect('admin-user-unlock')

@admin_required('home')
def make_admin(request, id):
    '''Makes admin from a user.'''
    if request.method=='POST':
        try:
            user = CustomUser.objects.get(id=id)
            # Since admins cannot lock their accounts nor can
            # request delete, we set the related values to default
            user.is_superuser = True
            user.unsuccessful_attempts = 0
            user.requested_delete = False
            user.requested_unlock = False
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