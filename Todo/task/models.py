from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(blank=False, max_length=120)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)