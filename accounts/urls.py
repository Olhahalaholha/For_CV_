from django.urls import path
from . import views
from django.contrib.auth import views as authentication_views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('login/', authentication_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', authentication_views.LoginView.as_view(template_name='registration/logout.html'), name='logout'),
]
