from django.contrib import admin

# Register your models here.

from .models import Workflow, Task

admin.site.register(Workflow)
admin.site.register(Task)