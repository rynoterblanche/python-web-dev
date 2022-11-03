from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

from workflows.models import Workflow


def welcome(request):
    return render(request, "website/welcome.html",
                  {"workflows": Workflow.objects.all()})


def date(request):
    return HttpResponse(f"This page was served at '{str(datetime.now())}'")


def about(request):
    return HttpResponse(f"This app is a demo")
