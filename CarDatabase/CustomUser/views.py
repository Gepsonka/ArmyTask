from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .decorators import not_admin_required
from django.contrib import messages

# Create your views here.

@login_required
@not_admin_required('home', 'Page is not for admin users!')
def user_request_delete_page_view(request):
    '''Sending the deletion request page to the user'''
    return render(request, 'CustomUser/templates/user_delete_request.html', None)


@login_required
@not_admin_required('home', 'Admins cannot request for account delete.')
def user_request_delete(request):
    '''
    Setting the user\'s requested_delete to the opposite value (negating the value).
    The view sends message depending on wether the user requested a delete
    or requested not to get deleted.
    Once the user set the request, he/she can remove it.
    '''
    if request.method == 'POST':
        request.user.requested_delete = not request.user.requested_delete
        request.user.save()
        if request.user.requested_delete:
            messages.success(request, 'Your account will soon be deleted by an admin.')
        else:
            messages.success(request, 'Your account now won\'t be deleted.')
        return redirect('home')

    return redirect('user-delete-request')
