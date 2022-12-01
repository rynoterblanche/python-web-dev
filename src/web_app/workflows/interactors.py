from typing import List

from core.entities.workflow_aggregate.workflow import Workflow
from core.interfaces.repositories.workflows import WorkflowRepository


class WorkflowInteractor:

    def __init__(self, workflows_repo: WorkflowRepository):
        self.workflows_repo = workflows_repo

    def get_all(self) -> List[Workflow]:
        return self.workflows_repo.list()

    def get_by_id(self, workflow_id: int) -> Workflow:
        return self.workflows_repo.get_by_id(workflow_id)
