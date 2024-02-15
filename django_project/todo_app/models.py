from django.db import models

from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from django.urls import reverse

def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)
# Create your models here.
class ToDoListModel(models.Model):
    title = models.CharField(max_length= 100, unique= True)

    def get_absolute_url(self):
        return reverse("list", args = [self.id])
    
    def __str__(self):
        return self.title


class Task(models.Model):
    
    class Priority(models.TextChoices):
        URGENT = "URGENT", _("Urgent")
        MEDIUM = "MEDIUM", _("Medium")
        LOW = "LOW", _("Low")


    title = models.CharField(max_length = 100)
    description = models.TextField(null=True, blank=True)
    priority = models.CharField(max_length = 6,default = Priority.LOW, choices = Priority)
    due_date = models.DateTimeField(default = one_week_hence)
    created_date = models.DateTimeField(auto_now_add=True)
    todo_list = models.ForeignKey(ToDoListModel, on_delete = models.CASCADE)
    done = models.BooleanField(default = False)
    
    def get_absolute_url(self):
        return reverse(
            "task-update", args = [str(self.todo_list.id), str(self.id)]
        )
    
    def __str__(self):
        return f"{self.title}: due {self.due_date}"
    
    

    class Meta:
        ordering = ["due_date"]