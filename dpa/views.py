from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from dpa.forms import RegistrationForm


# Create your views here.
def home(request):
    return render(request, "home.html")

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print("ITS VALID")
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registered successfully!")
            return redirect("home")
        else:
            messages.success(request, "Please correct the validation errors.")
            print(form.errors)
            return render(request, "register.html", {"form": form})
    else:
        return render(request, "register.html")

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, "Invalid username or password.")
            return redirect('login')
    else:
        return render(request, "login.html")

def logout_user(request):
    logout(request)
    messages.success(request, "You have logged out successfully.")
    return redirect('home')

def forgot_password(request):
    return render(request, "forgot-password.html")
