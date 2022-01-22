from django.db import models
from django.forms import CharField

# Create your models here.

class List(models.Model):
    """todolist model"""
    task = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.task + '|' + str(self.completed)