from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    text = models.TextField()
    image = models.ImageField(upload_to='blog/images/', blank=True)
