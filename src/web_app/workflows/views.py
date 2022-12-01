from django.shortcuts import render, get_object_or_404, redirect

from .forms import WorkflowForm
from .models import WorkflowModel, TaskModel
from .serializers import WorkflowsListSerializer, WorkflowSerializer


class WorkflowsView:

    def __init__(self, request, workflow_interactor=None):
        self.request = request
        self.workflow_interactor = workflow_interactor

    def get(self):
        workflows = self.workflow_interactor.get_all()

        body = {"workflows": WorkflowsListSerializer.serialize(workflows)}

        return render(self.request, "workflows/list.html", body)


class WorkflowDetailView:

    def __init__(self, request, workflow_interactor=None):
        self.request = request
        self.workflow_interactor = workflow_interactor

    def get(self, id: int):
        workflow = self.workflow_interactor.get_by_id(id)

        body = {"workflow": WorkflowSerializer.serialize(workflow)}

        return render(self.request, "workflows/detail.html", body)


def tasks_list(request):
    return render(request, "workflows/tasks_list.html",
                  {"tasks": TaskModel.objects.all()})


def new(request):
    if request.method == "POST":
        form = WorkflowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = WorkflowForm()
    return render(request, "workflows/new.html", {"form": form})


def edit(request, id):
    workflow = get_object_or_404(WorkflowModel, pk=id)
    if request.method == "POST":
        form = WorkflowForm(request.POST, instance=workflow)
        if form.is_valid():
            form.save()
            return redirect("detail", id)
    else:
        form = WorkflowForm(instance=workflow)
    return render(request, "workflows/edit.html", {"form": form})


def delete(request, id):
    workflow = get_object_or_404(WorkflowModel, pk=id)
    if request.method == "POST":
        workflow.delete()
        return redirect("welcome")
    else:
        return render(request, "workflows/confirm_delete.html", {"workflow": workflow})
