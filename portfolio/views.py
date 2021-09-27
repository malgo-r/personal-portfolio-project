from django.shortcuts import render
from django.http import HttpResponse
from portfolio.templates import portfolio
from .models import Project


def home(request):
    projects = Project.objects.all()  # this grabs all the objects from the db which are the project objects
    return render(request, 'portfolio/home.html', {'projects': projects})
