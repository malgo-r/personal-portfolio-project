from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)  # https://docs.djangoproject.com/en/3.2/ref/models/fields/#field-types
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)  # blank can be added everywhere

    def __str__(self):
        return self.title  # this cause that in admin/ there is no entry likr Project(1), Project(2) but real title of project
