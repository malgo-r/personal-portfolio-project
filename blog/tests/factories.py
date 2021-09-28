import factory
from django.db import models as django_models

from blog.models import Blog


class BlogFactory(factory.Factory):

    class Meta:
        model = Blog

    title = "Sample blog title"
    date = django_models.DateField(auto_now=True)
    text = "Sample blog text"
