from django.shortcuts import render, redirect
from .register_form import LibSignUpForm, StudSignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.


def lib_register(request):
    if request.method == 'POST':
        form = LibSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "account created successfully!")
            return redirect('login')

        else:
            form = LibSignUpForm()
            return render(request, 'accounts/register.html', {'form': form})
    form = LibSignUpForm(request.POST)
    return render(request, 'accounts/register.html', {'form': form})


def stud_register(request):
    if request.method == 'POST':
        form = StudSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "account created successfully!")
            return redirect('login')

        else:
            form = StudSignUpForm()
            return render(request, 'accounts/register.html', {'form': form})
    form = StudSignUpForm(request.POST)
    return render(request, 'accounts/register.html', {'form': form})


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "you are logged in.")
            return redirect('available_books')
        else:
            messages.error(request, "oops! login failed.")
            return redirect('login')
    return render(request, 'accounts/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "logged out successfully!")
    return render(request, 'base/index.html')
