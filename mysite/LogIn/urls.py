from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.signin, name='home'),
    path('home', views.home, name='home'),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path('homepage',views.homepage_view,name = 'homepage')
]
