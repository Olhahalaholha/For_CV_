from django.contrib import admin
from .models import Anketa


class ReturnComAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'address', 'phone', 'modified_date')


admin.site.register(Anketa, ReturnComAdmin)
