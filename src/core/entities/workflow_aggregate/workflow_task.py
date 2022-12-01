from enum import Enum
from typing import Dict, Any


class TaskState(Enum):
    PENDING = 1
    RUNNING = 2
    COMPLETE = 3


class WorkflowTask:
    id: int
    command: str
    parameters: Dict[str, Any]
    state: TaskState

    def __init__(self, id: int, command: str, parameters: Dict[str, Any]):
        self.id = id
        self.command = command
        self.parameters = parameters
        self.state = TaskState.PENDING

    @property
    def is_done(self):
        return self.state == TaskState.COMPLETE
