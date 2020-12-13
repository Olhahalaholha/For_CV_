from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.db import models
from django.utils import timezone

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have a username')
        user = self.model(
            username=self.model.normalize_username(username),)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username, password=password,)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200, verbose_name='username', unique=True)
    email = models.EmailField(max_length=254)
    date_joined = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    password = models.CharField(max_length=200)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)  # a superuser


    objects = UserManager()

    class Meta:
        managed = True
        verbose_name_plural = "Пользователи"





# class CustomUser(AbstractBaseUser):
#     id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=200, verbose_name='username', unique=True)
#     email = models.EmailField(max_length=254)
#     date_joined = models.DateTimeField(default=timezone.now)
#     password = models.CharField(max_length=200)
#
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = []
#
#     objects = UserAccountManager()
#
#     def __str__(self):
#         return self.username
#
#     class Meta:
#         managed = True
#         verbose_name_plural = "Пользователи"
