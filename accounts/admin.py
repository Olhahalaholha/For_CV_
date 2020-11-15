from django.contrib import admin
from .models import CustomUser


class ReturnComAdmin(admin.ModelAdmin):
    list_display = ('username','email')


admin.site.register(CustomUser, ReturnComAdmin)