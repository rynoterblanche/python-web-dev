from workflows.interactors import GetAllWorkflowsInteractor
from workflows.repositories import DjangoWorkflowsRepository
from workflows.views import WorkflowsView


def create_workflows_repo():
    return DjangoWorkflowsRepository()


def create_get_all_workflows_interactor():
    return GetAllWorkflowsInteractor(workflows_repo=create_workflows_repo())


def create_workflows_view(request, **kwargs):
    return WorkflowsView(request=request,
                         get_all_workflows_interactor=create_get_all_workflows_interactor())
