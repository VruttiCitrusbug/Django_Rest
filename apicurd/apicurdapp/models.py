from django.db import models

# Create your models here.
class book(models.Model):
    title=models.CharField(max_length=100)
    price=models.IntegerField()
    totalpage=models.IntegerField()
    auther=models.CharField(max_length=100)
    def __str__(self):
        return self.title
class auther(models.Model):
    name=models.CharField(max_length=100)
    bookname=models.CharField(max_length=100)
    def __str__(self):
        return self.name