from django.shortcuts import render
from .models import Blog


def all_blogs(request):
    entries = Blog.objects.order_by('-date')[:5]  # show only 5 latest posts
    return render(request, 'blog/all_blogs.html', {'entries': entries})
