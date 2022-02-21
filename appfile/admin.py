from django.contrib import admin
from .models import given_task,TodoListItem
# Register your models here.
admin.site.register(given_task)
admin.site.register(TodoListItem)