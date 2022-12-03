from django.shortcuts import render

from workflows.models import WorkflowModel


def welcome(request):
    return render(request, "website/welcome.html",
                  {"workflow": WorkflowModel.objects.all()})
