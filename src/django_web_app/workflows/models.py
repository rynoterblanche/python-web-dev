from django.db import models


class Workflow(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Task(models.Model):
    command = models.CharField(max_length=200)
    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE)

    def __str__(self):
        return f"Command: '{self.command}' - running in '{self.workflow}'"
