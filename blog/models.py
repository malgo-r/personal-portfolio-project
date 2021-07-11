from django.db import models


class Blog(models.Model):  # only properties in models class need migrations. function do not
    title = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    text = models.TextField()
    image = models.ImageField(upload_to='blog/images/', blank=True)

    def __str__(self):
        return self.title  # this cause that in admin/ there is no entry like Blog(1), Blog(2) but real title of project