from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import ensure_csrf_cookie
from django.middleware.csrf import get_token
from django.http import HttpResponse


# Create your views here.

def home(request):
    # check to see if user is logged in
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            # authenticate
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have been logged in")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password")
                return redirect('home')
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('home')
    else:
        response = render(request, 'home.html', {})
        # Ensure the CSRF cookie is set
        response.set_cookie('csrftoken', get_token(request))
        return response


def login_user(request):
    pass


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out ...")
    return redirect('home')


def register_user(request):
    return render(request, 'register.html', {})
