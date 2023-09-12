from django.shortcuts import render, redirect
from .forms import SignInForms, SignUpForms
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Users

# Create your views here.

def SignIn(request):
    if request.method == "POST":
        form = SignInForms(data=request.POST)
        if form.is_valid():
            users = form.get_user()
            login(request, users)
            return redirect("home")
    else:
        form = SignInForms()
    return render(request, "signin.html", {"form":form})

def SingUp(request):
    if request.method == "POST":
        form = SignUpForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
    else:
        form = SignUpForms()
    return render(request, "signup.html", {"form":form})

def logoutpage(request):
    logout(request)
    return redirect("signin")

