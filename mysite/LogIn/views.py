from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate

# Create your views here.
def home(request):
        return render(request, "LogIn/index.html")

def signup(request):
        if request.method == 'POST':
                username = request.POST['username']
                email = request.POST['email']
                fname = request.POST['firstname']
                lname = request.POST['lastname']
                pass1 = request.POST['pass1']
                pass2 = request.POST['pass2']
                #while(pass1 != pass2):
                        
                        #messages.error(request, 'Passwords do not match')
                myuser = User.objects.create_user(username, email, pass1, unlocked = 1)
                myuser.firstname = fname
                myuser.lastname = lname

                myuser.save()

                messages.success(request, "Your account has been successfully created")
                return redirect('home')


        return render(request, "LogIn/signup.html")
        
def signin(request):
        return render(request, "LogiIn/signin.html")

def signout(request):
        pass
