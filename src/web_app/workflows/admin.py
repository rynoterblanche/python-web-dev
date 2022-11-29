from django.contrib import admin

# Register your models here.

from .models import WorkflowModel, TaskModel

admin.site.register(WorkflowModel)
admin.site.register(TaskModel)