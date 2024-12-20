from django.test import TestCase
from myapp.forms import TodolistForm

class TodolistFormTestCase(TestCase):
    def test_valid_form(self):
        data = {"text": "New Task", "completed": False}
        form = TodolistForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {"text": ""}
        form = TodolistForm(data=data)
        self.assertFalse(form.is_valid())