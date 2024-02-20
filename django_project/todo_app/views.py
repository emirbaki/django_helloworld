from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.contrib import messages
# Create your views here.
from .models import ToDoListModel, Task

from .forms import TodoForm, TaskForm

class ToDoListView(ListView):
    model = ToDoListModel

class TaskView(ListView):
    model = Task

def ToDoListPage(req):
    ToDoLists = ToDoListModel.objects.all

    if req.method == "POST":
        if 'taskForm_Btn' in req.POST:
            initial_Data = req.POST.get('taskForm_Btn')
            taskform = TaskForm(req.POST)
            t = taskform.save(commit=False)
            t.todo_list = ToDoListModel.objects.get(id = initial_Data)
            if taskform.is_valid():
                # t.todo_list = ToDoListModel.objects.get(id = initial_Data)
                t.save()
                return redirect('todolists')
        if 'todolistForm_Btn' in req.POST:
            form = TodoForm(req.POST)
            if form.is_valid():
                form.save()
                return redirect('todolists')

    form = TodoForm()

    taskForm = TaskForm()

    context = {
        "forms": form,
        "taskForms" : taskForm,
        "todolists" : ToDoLists,
        "tasks" : Task.objects.all
    }
    return render(req, '../templates/todo_app/todolistmodel_list.html', context)

def remove(request, item_id):
    item = ToDoListModel.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todolists')