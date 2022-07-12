from django.db import models

# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=2000, blank=False, null=False)
    due_date=models.DateField()
