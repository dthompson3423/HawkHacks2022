from re import template
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm, UpdateProfileForm
from django.contrib import messages
from django.db.models import Q
import json


# Create your views here.
def home(request):
        return render(request, "LogIn/index.html")

def signup(request):
        user = request.user
        
        if request.method == 'POST':
                user_form = RegisterForm(request.POST)
                prof_form = UpdateProfileForm(request.POST)
                if user_form.is_valid and prof_form.is_valid:
                        username = request.POST['username']
                        email = request.POST['email']
                        if authenticate(username=username) is not None and authenticate(email=email) is not None and request.POST['password1'] == eequest.POST['password2']:
                                prof_form.save()
                                messages.success(request, "Your account has been successfully created")
                                return render(request, "Homepage/homepage.html")
                messages.error(request, "Could not create an account")
        return render(request, "LogIn/signup.html")
        
def signin(request):
        user = request.user

        if user.is_authenticated:
                return redirect('home')
        
        if request.POST:
                form = LoginForm(request.POST)
                if form.is_valid():
                        email = request.POST['email']
                        password = request.POST['password']
                        user = authenticate(email=email,password = password)

                if user:
                        login(request,user)
                        print("HTE")
                        return redirect('signup')
        else:
                form = LoginForm()
        
        context = {
                'form':form
        }
        template_name = "Login/signin.html"
        return render(request = request, template_name= template_name,context= context )

def signout(request):
        pass
