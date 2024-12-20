from django import forms
from myapp.models import Todolist

class TodolistForm(forms.ModelForm):
    class Meta:
        model = Todolist
        fields = ["text", "completed"]