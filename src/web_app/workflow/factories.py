from src.web_app.workflow.interactors import WorkflowInteractor
from src.web_app.workflow.repositories import DjangoWorkflowsRepository
from src.web_app.workflow.views import WorkflowsView, WorkflowDetailView


def create_workflows_repo() -> DjangoWorkflowsRepository:
    return DjangoWorkflowsRepository()


def create_workflow_interactor() -> WorkflowInteractor:
    return WorkflowInteractor(workflows_repo=create_workflows_repo())


def create_workflows_view(request, **kwargs) -> WorkflowsView:
    return WorkflowsView(request=request,
                         workflow_interactor=create_workflow_interactor())


def create_workflow_detail_view(request, **kwargs) -> WorkflowDetailView:
    return WorkflowDetailView(request=request,
                              workflow_interactor=create_workflow_interactor())
