from email.policy import default
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.

class post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=13)
    slug = models.CharField(max_length=130)
    content= models.TextField()
    views = models.IntegerField(default=0) 
    images = models.ImageField(upload_to='')
    Timestamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title +" By "+ self.author

class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user= models.ForeignKey(User , on_delete=models.CASCADE)
    Post =models.ForeignKey(post,on_delete=models.CASCADE)
    parent = models.ForeignKey('self' , on_delete=models.CASCADE , null=True)
    Timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username
    

