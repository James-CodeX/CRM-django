from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import ensure_csrf_cookie
from django.middleware.csrf import get_token
from django.http import HttpResponse
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.


def home(request):
    records = Record.objects.all()
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
        response = render(request, 'home.html', {'records': records})
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
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # authenticate and login
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password1')
            )
            login(request, user)
            messages.success(request, "You have successfully registered")
            return redirect('home')
        else:
            messages.error(
                request, "Unsuccessful registration. Invalid information.")
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        # lookup records
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(
            request, "You must be logged in to view this page ...")
        return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record deleted successfully ...")
        return redirect('home')
    else:
        messages.success(
            request, "You must be logged in to delete a record ...")


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "Record added ...")
                return redirect('home')
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.success(request, "You must be logged in to add a record ...")
        return redirect('home')


def update_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=customer_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record updated ...")
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.success(
            request, "You must be logged in to update a record ...")
