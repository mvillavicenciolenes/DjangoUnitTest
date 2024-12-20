from django.test import TestCase
from myapp.models import Todolist

class TodolistModelTestCase(TestCase):
    def setUp(self):
        self.task1 = Todolist.objects.create(text="Task 1", completed=False)
        self.task2 = Todolist.objects.create(text="Task 2", completed=True)

    def test_todolist_creation(self):
        self.assertEqual(self.task1.text, "Task 1")
        self.assertFalse(self.task1.completed)

    def test_todolist_str_representation(self):
        self.assertEqual(str(self.task1), "Task 1")

    def test_todolist_default_completed_false(self):
        new_task = Todolist.objects.create(text="New Task")
        self.assertFalse(new_task.completed)