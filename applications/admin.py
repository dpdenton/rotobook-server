from django.contrib import admin

# Register your models here.
from applications.models import Employee

admin.site.register(Employee)
