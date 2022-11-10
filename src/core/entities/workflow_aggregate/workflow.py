from typing import List

from src.core.entities.workflow_aggregate.workflow_task import WorkflowTask


class Workflow:
    id: int
    name: str
    tasks: List[WorkflowTask]

    def __init__(self, id: int, name: str, tasks: List[WorkflowTask]):
        self.id = id
        self.name = name
        self.tasks = tasks

    @property
    def is_complete(self) -> bool:
        if all(task.is_done for task in self.tasks):
            return True

        return False

    def execute(self) -> None:
        # TODO - submit / execute tasks (async operation)
        raise NotImplementedError()
