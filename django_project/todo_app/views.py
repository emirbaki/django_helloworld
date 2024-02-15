from django.shortcuts import render
from django.views.generic.list import ListView
# Create your views here.
from .models import ToDoListModel, Task


class ToDoListView(ListView):
    model = ToDoListModel

class TaskView(ListView):
    model = Task

def ToDoListPage(req):
    ToDoLists = ToDoListModel.objects.all
    context = {
        "todolists" : ToDoLists,
        "tasks" : Task.objects.all
    }
    return render(req, '../templates/todo_app/todolistmodel_list.html', context)

