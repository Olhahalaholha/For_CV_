from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from accounts.models import CustomUser


class Anketa(models.Model):
    surname = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    modified_date = models.DateTimeField(default=timezone.now)
    name = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.phone

    class Meta:
        managed = True
        verbose_name_plural = "Анкеты"
