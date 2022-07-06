from django.shortcuts import render, redirect
from .register_form import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "account created successfully!")
            return redirect('login')

        else:
            form = SignUpForm()
            return render(request, 'accounts/register.html', {'form': form})
    form = SignUpForm(request.POST)
    return render(request, 'accounts/register.html', {'form': form})


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "you are logged in.")
            return redirect('add_book')
        else:
            return redirect('login')

    return render(request, 'accounts/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "logged out successfully!")
    return redirect('home')
