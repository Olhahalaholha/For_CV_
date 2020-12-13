from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegisterForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = get_user_model()
        fields = 'username', 'email', 'password1', 'password2'


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')
