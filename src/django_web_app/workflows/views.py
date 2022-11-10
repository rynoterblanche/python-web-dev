from django.shortcuts import render, get_object_or_404, redirect

from workflows.forms import WorkflowForm
from workflows.models import WorkflowModel, TaskModel
from workflows.serializers import WorkflowsListSerializer


class WorkflowsView:

    def __init__(self, request, get_all_workflows_interactor=None):
        self.request = request
        self.get_all_workflows_interactor = get_all_workflows_interactor

    def get(self):
        workflows = self.get_all_workflows_interactor.execute()

        body = {"workflows": WorkflowsListSerializer.serialize(workflows)}

        return render(self.request, "workflows/list.html", body)


def detail(request, id):
    workflow = get_object_or_404(WorkflowModel, pk=id)
    return render(request, "workflows/detail.html", {"workflow": workflow})


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
