""" Users views. """

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Exception
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User
from users.models import Profile


def login_view(request):
    """Login view."""
    #import pdb; pdb.set_trace()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('n_posts')
        else:
            return render (
                request, 
                'users/login.html',
                {
                    'error': 'Invalid username and password'
                }
            )

    return render(
        request, 
        'users/login.html'
    )


def signup(request):
    """Sign up view."""
    if request.method == 'POST':
        v_username = request.POST['username']
        v_passwd = request.POST['passwd']
        v_passwd_confirmation = request.POST['passwd_confirmation']

        if v_passwd != v_passwd_confirmation:
            return render(
                request,
                'users/signup.html',
                {
                    'error': 'Password confirmation does not match!'
                }
            )
        try:
            user = User.objects.create_user(username=v_username, password=v_passwd)
        except IntegrityError:
            return render(
                request,
                'users/signup.html',
                {
                    'error': 'Username is already in use!'
                }
            )                  
                
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        profile = Profile(user=user)
        profile.save()

        return redirect('n_users-login')
        
    return render(request, 'users/signup.html')


@login_required
def logout_view(request):
    """Logout a user."""
    logout(request)

    return redirect('n_users-login')