from django.urls import path
from . import views
from .views import MyLoginView
from django.contrib.auth.views import LogoutView


urlpatterns = (
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('login/', MyLoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
)
