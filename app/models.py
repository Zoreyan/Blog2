from django.db import models


class Post(models.Model):
    image = models.ImageField(upload_to='images/', null=True)
    title = models.CharField(max_length=25)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)