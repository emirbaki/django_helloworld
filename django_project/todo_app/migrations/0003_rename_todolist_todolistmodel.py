# Generated by Django 5.0.2 on 2024-02-14 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_task_description_task_priority'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ToDoList',
            new_name='ToDoListModel',
        ),
    ]
