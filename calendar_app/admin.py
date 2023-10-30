from django.contrib import admin
from .models import TodoModel

# Register your models here.python manage.py makemigrations
admin.site.register(TodoModel)