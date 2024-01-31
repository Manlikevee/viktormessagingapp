from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages




# Create your views here.

def not_authenticated(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            messages.error(request, 'you are already logged in')
            return redirect('superdashboard')  # Replace with the URL name or path of the superuser page
    return wrapper


def superuser_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('userdashboard')  # Replace with the URL name or path of the non-superuser page
    return wrapper


@not_authenticated
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Welcome to your dashboard. ')
            return redirect('userdashboard')  # Replace 'home' with the name of your desired homepage URL
        else:
            messages.error(request, 'Invalid Account ID or Password. ')

    return render(request, 'login.html')
