from django.db import models

from django.conf import settings
from django.utils import timezone


class to_do_list(models.Model):
    task = models.CharField(max_length=200)
    description = models.TextField()
    date=models.DateTimeField(default=timezone.now)
    
    def save(self):
        self.save()
    
    def task_to_string(self):
        return self
    