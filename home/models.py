import email
from importlib.resources import contents
from sqlite3 import Timestamp
from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    content= models.TextField()
    Timestamp = models.DateTimeField(auto_now_add=True , blank=True)


    def __str__(self):
        return "Message From : " + self.name