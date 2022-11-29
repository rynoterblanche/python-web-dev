from django.db import models


class WorkflowModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class TaskModel(models.Model):
    id = models.IntegerField(primary_key=True)
    command = models.CharField(max_length=200)
    workflow = models.ForeignKey(WorkflowModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"Command: '{self.command}' - running in '{self.workflow}'"
