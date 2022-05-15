from pyexpat import model
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from myapp.models import Account


# Registration Form
class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=60)
    last_name = forms.CharField(max_length=60)

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "username", "password1", "password2")

# Login Form
class LoginForm(UserCreationForm):
    password = forms.CharField(label = 'Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']

            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid email/password")

# Edit Profile Form
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'bio', 'location')