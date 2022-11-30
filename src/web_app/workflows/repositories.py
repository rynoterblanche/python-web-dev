from typing import List

from src.core.entities.workflow_aggregate.workflow import Workflow
from src.core.entities.workflow_aggregate.workflow_task import WorkflowTask
from src.core.interfaces.repositories.workflows import WorkflowRepository
from workflows.models import WorkflowModel, TaskModel


class DjangoWorkflowsRepository(WorkflowRepository):

    def get_by_id(self, workflow_id: int) -> Workflow:
        raise NotImplementedError()

    def list(self) -> List[Workflow]:
        workflow_models = WorkflowModel.objects.all()

        return [self._map_workflow(model) for model in workflow_models]

    def _map_workflow(self, model: WorkflowModel) -> Workflow:
        task_models = TaskModel.objects.all()
        return Workflow(id=model.id,
                        name=model.name,
                        tasks=[self._map_task(model) for model in task_models])

    def _map_task(self, task_model: TaskModel) -> WorkflowTask:
        return WorkflowTask(id=task_model.id,
                            command=task_model.command,
                            parameters={})
