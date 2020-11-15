from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import CustomUser
from django.contrib import messages


def home(request):
	return render(request, "home/home.html")


def register(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		warning = f'Вы вошли на сайт.'
		if form.is_valid():
			username = form.cleaned_data.get("username")
			warning =  f'Пользователь {username} зарегестрирован.'
			messages.success(request, warning)
			form.save()
			return redirect("login")
		else:
		    for msg in form.error_messages:
        		messages.error(request, f"{msg}: {form.error_messages[msg]}")
        		print(msg)
			# for msg in form.error_messages:
			# 	messages.error(request, f"{msg}: {form.error_messages[msg]}")

		# 	password1 = form.cleaned_data.get("password1")
		# 	password2 = form.cleaned_data.get("password2")
		# 	username = form.cleaned_data.get("username")
		# 	email = form.cleaned_data.get("email")
		# 	if password2 != password1:
		# 		messages.error(request, 'Пароли password1 и password2 не совпадают.')
		# 		form.add_error('password1', messages)
		# 		form.add_error('password2', messages)

			# if CustomUser.objects.filter(username=username).exists():
			# 	messages.info(request, f"Пользователь с таким именем существует.")
			# if CustomUser.objects.filter(email=email).exists():
			#  	warning = f"Почта с таким именем есть у другого пользователя."
			#  	messages.success(request, warning)
		    #messages.success(request, warning)
	form = RegisterForm()
	return render(request, "registration/register.html", {"form":form})