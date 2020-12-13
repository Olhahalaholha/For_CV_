from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView
from .forms import RegisterForm, LoginForm


class MyLoginView(LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'

# class MyLoginView(LoginView):
#     template_name = 'registration/login.html'
#     success_url = "page_main"
#     success_message = 'Вы вошли на сайт'


def home(request):
    return render(request, "home/home.html")


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f'Пользователь {username} зарегестрирован.')
            return redirect("login")
        else:
            messages.info(request, form.errors)
    return render(request, "registration/register.html", {"form": form})
