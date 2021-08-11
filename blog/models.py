from django.db import models
from django.urls import  reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    body = models.TextField(max_length=100)

    def __str__(self):
        return self.title



