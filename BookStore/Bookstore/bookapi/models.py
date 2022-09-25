from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Books(models.Model):
    bookname=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    price=models.IntegerField()
    qty=models.IntegerField()
    publisher=models.CharField(max_length=200)
    def __str__(self):
        return self.bookname
