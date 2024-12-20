from django.contrib import admin
from myapp.models import Todolist

@admin.register(Todolist)
class TodolistAdmin(admin.ModelAdmin):
    list_display = ("text", "completed")