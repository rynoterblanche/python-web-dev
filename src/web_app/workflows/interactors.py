from core.interfaces.repositories.workflows import WorkflowRepository


class WorkflowInteractor:

    def __init__(self, workflows_repo: WorkflowRepository):
        self.workflows_repo = workflows_repo

    def get_all(self):
        return self.workflows_repo.list()

    def get_by_id(self, workflow_id: int):
        return self.workflows_repo.get_by_id(workflow_id)
