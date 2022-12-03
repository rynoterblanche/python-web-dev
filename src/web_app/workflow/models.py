from django.db import models


class Workflow(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'workflow'
        verbose_name_plural = 'workflow'

    def __str__(self):
        return self.name


class Task(models.Model):
    id = models.IntegerField(primary_key=True)
    command = models.CharField(max_length=200)
    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE)

    def __str__(self):
        return f"Command: '{self.command}' - running in '{self.workflow}'"
