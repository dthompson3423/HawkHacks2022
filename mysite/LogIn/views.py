from re import template
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm, UpdateProfileForm
from django.contrib.auth.models import User
from myapp.models import Account, AccountManager
from django.contrib import messages
from django.db.models import Q
import json


# Create your views here.
def home(request):
        return render(request, "LogIn/index.html")

def signup(request):
        if request.method == 'POST':
                username = request.POST['username']
                email = request.POST['email']
                fname = request.POST['firstname']
                lname = request.POST['lastname']
                pass1 = request.POST['password1']
                pass2 = request.POST['password2']

                if authenticate(username) is None and authenticate(email) is None and pass1==pass2:
                        myuser = User.objects.create_user(username, email, pass1)
                        myuser.unlocked = 1
                        myuser.firstname = fname
                        myuser.lastname = lname

                        myuser.save()

                        messages.success(request, "Your account has been successfully created")

                        return redirect('signin')
                messages.error(request, "Account cannot be created!")
        return render(request, "LogIn/signup.html")

def signin(request):
        if request.method == 'POST':
                username = request.POST['username']
                password = request.POST['password']

                user = authenticate(username=username, password=password)

                if user is not None:
                        login(request, user)
                        fname = user.first_name
                        return render(request, "Homepage/homepage.html", {'fname': fname})
        messages.error(request, "Unable to login!")
        return render(request, "LogIn/index.html")

def signout(request):
        pass
