from unicodedata import name
from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    desc=models.TextField()
    dtenroll=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name