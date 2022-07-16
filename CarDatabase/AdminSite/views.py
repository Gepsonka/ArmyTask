from email.utils import parseaddr
from django.shortcuts import render, redirect
from CustomUser.models import CustomUser
from django.contrib import messages
from .forms import AdminUserCreationForm
from CustomUser.decorators import admin_user_required



# Create your views here.
@admin_user_required('admin-login')
def users_page_view(request):
    # # If user is not authenticated redirect home
    # if not request.user.is_authenticated:
    #     messages.warning(request, 'Log in first as admin!')
    #     return redirect('admin-login')

    # # If user is not admin redirect to home
    # if not request.user.is_staff and not request.user.is_superuser:
    #     return redirect('home')

    # Return the lis of all users to the template
    all_users = CustomUser.objects.all()
    return render(request, 'AdminSite/templates/users.html', {'all_users': all_users})


def user_creation_view(request):
    '''View to create users by the admins. 
    By default an admin can select any password se/he likes.
    The view checks if there are any users with the same username or password,
    if there is not any create a new user with the given credentials, else send error.'''

    # If user is not authenticated redirect home
    if not request.user.is_authenticated:
        messages.warning(request, 'Log in first as admin!')
        return redirect('admin-login')

    # If user is not admin redirect to home
    if not request.user.is_staff and not request.user.is_superuser:
        return redirect('home')
    
    if request.method=='POST':
        form = AdminUserCreationForm(request.POST)
        

        if form.is_valid():
            # Check if user with the same username or email exists
            try:
                # If user does not exists thee xpression below throws
                # an exeption so the user can be created
                CustomUser.objects.get(username=form.cleaned_data.get('username'))
                messages.error(request, 'User with the same username already exists!')
                return render(request, 'AdminSite/templates/admin_user_creation.html', {'form':form})
            except:
                pass

            try:
                CustomUser.objects.get(email=form.cleaned_data.get('email'))
                messages.error(request, 'User with the same email already exists!')
                return render(request, 'AdminSite/templates/admin_user_creation.html', {'form':form})
            except:
                pass

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
    else:
        form = AdminUserCreationForm()

    return render(request, 'AdminSite/templates/admin_user_creation.html', {'form':form})

def user_delete_page_view(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Log in first as admin!')
        return redirect('admin-login')

    if not request.user.is_superuser and not request.user.is_staff:
        return redirect('home')

    delete_request_users = CustomUser.objects.filter(requested_delete=True)

    return render(request, 'AdminSite/templates/admin_user_delete.html', {'delete_request_users': delete_request_users})


def user_delete_view(request, id):
    if not request.user.is_authenticated:
        messages.warning(request, 'Log in first as admin!')
        return redirect('admin-login')

    if not request.user.is_superuser and not request.user.is_staff:
        return redirect('home')

    try:
        CustomUser.objects.get(id=id).delete()
        messages.success(request, 'User was successfully deleted')

        # Have to redirect back to the admin-users page bc otherwise
        # it would not refresh the list
        return redirect('admin-users')
    except:
        messages.error(request, "Error! User does not exists!")

def user_unlock_view(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Log in first as admin!')
        return redirect('admin-login')

    if not request.user.is_superuser and not request.user.is_staff:
        return redirect('home')

    


