from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404, redirect

from src.web_app.workflow.forms import WorkflowForm
from src.web_app.workflow.interactors import WorkflowInteractor
from src.web_app.workflow.models import Workflow, Task
from src.web_app.workflow.serializers import WorkflowsListSerializer, WorkflowSerializer


class WorkflowsView:

    def __init__(self, request: HttpRequest, workflow_interactor: WorkflowInteractor):
        self.request = request
        self.workflow_interactor = workflow_interactor

    def get(self) -> HttpResponse:
        workflows = self.workflow_interactor.get_all()

        body = {"workflows": WorkflowsListSerializer.serialize(workflows)}

        return render(self.request, "workflow/list.html", body)


class WorkflowDetailView:

    def __init__(self, request: HttpRequest, workflow_interactor: WorkflowInteractor):
        self.request = request
        self.workflow_interactor = workflow_interactor

    def get(self, id: int) -> HttpResponse:
        workflow = self.workflow_interactor.get_by_id(id)

        body = {"workflow": WorkflowSerializer.serialize(workflow)}

        return render(self.request, "workflow/detail.html", body)


def tasks_list(request):
    return render(request, "workflow/tasks_list.html",
                  {"tasks": Task.objects.all()})


def new(request):
    if request.method == "POST":
        form = WorkflowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = WorkflowForm()
    return render(request, "workflow/new.html", {"form": form})


def edit(request, id):
    workflow = get_object_or_404(Workflow, pk=id)
    if request.method == "POST":
        form = WorkflowForm(request.POST, instance=workflow)
        if form.is_valid():
            form.save()
            return redirect("detail", id)
    else:
        form = WorkflowForm(instance=workflow)
    return render(request, "workflow/edit.html", {"form": form})


def delete(request, id):
    workflow = get_object_or_404(Workflow, pk=id)
    if request.method == "POST":
        workflow.delete()
        return redirect("welcome")
    else:
        return render(request, "workflow/confirm_delete.html", {"workflow": workflow})
