from django.contrib import admin
from .models import CustomUser


class ReturnComAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'username',
                    'email',
                    'password',
                    'date_joined']


admin.site.register(CustomUser, ReturnComAdmin)
