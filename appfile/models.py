from django.db import models

from django.conf import settings
from django.utils import timezone


class given_task(models.Model):
    task = models.CharField(max_length=200)
    description = models.TextField()
    date=models.DateField()
    
#     # def save(self):
#     #     self.save()
    
    def task_to_string(self):
        return self
    
    
    
class TodoListItem(models.Model):
   tsk = models.TextField()  
    