from django.contrib import admin

from todo_app.models import ToDoList, Task
# Register your models here.
admin.site.register(Task)
admin.site.register(ToDoList)