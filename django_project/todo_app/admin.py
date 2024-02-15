from django.contrib import admin

from todo_app.models import ToDoListModel, Task
# Register your models here.
admin.site.register(Task)
admin.site.register(ToDoListModel)