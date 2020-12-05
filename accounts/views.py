from django.shortcuts import render, redirect
#from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
from .forms import RegisterForm


class MyLoginView(SuccessMessageMixin, LoginView):
    template_name = 'registration/login.html'
    success_url = "page_main"
    success_message = 'Вы вошли на сайт'


def home(request):
    return render(request, "home/home.html")


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        # if request.CustomUser.is_authenticated():
        #     messages.success(request, 'Вы вошли на сайт')
        if form.is_valid():
            username = form.cleaned_data.get("username")
            warning = f'Пользователь {username} зарегестрирован.'
            messages.success(request, warning)
            form.save()
            return redirect("login")
        else:
            username = form.cleaned_data.get("username")
            messages.info(request, form.errors)
    return render(request, "registration/register.html", {"form": form})
