from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
        return render(request, "Login/index.html")

def signup(request):
        return render(request, "Login/signup.html")

def signin(request):
        return render(request, "Login/signin.html")

def signout(request):
        pass
