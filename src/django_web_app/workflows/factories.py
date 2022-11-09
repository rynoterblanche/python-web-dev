from workflows.interactors import GetAllWorkflowsInteractor
from workflows.repositories import WorkflowsRepo
from workflows.views import WorkflowsView


def create_workflows_repo():
    return WorkflowsRepo()


def create_get_all_workflows_interactor():
    return GetAllWorkflowsInteractor(workflows_repo=create_workflows_repo())


def create_workflows_view(request, **kwargs):
    return WorkflowsView(request=request,
                         get_all_workflows_interactor=create_get_all_workflows_interactor())
