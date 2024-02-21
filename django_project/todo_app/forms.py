from django import forms
from .models import ToDoListModel, Task

class TodoForm(forms.ModelForm):
    class Meta:
        model = ToDoListModel
        fields = "__all__"

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title","description","priority","due_date"]