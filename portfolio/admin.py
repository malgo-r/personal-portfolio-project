from django.contrib import admin
from .models import Project


admin.site.register(Project)  # hey I want to see this model inside the admin, in localhost:800/admin/ now you can see Projects table