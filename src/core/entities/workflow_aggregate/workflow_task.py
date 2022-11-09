import uuid
from enum import Enum
from typing import Dict, Any


class TaskState(Enum):
    PENDING = 1
    RUNNING = 2
    COMPLETE = 3


class WorkflowTask:
    id: uuid.UUID
    command: str
    parameters: Dict[str, Any]
    state: TaskState

    def __init__(self, command: str, parameters: Dict[str, Any]):
        self.id = uuid.uuid4()
        self.command = command
        self.parameters = parameters
        self.state = TaskState.PENDING

    def run(self) -> None:
        self.state = TaskState.RUNNING

        # TODO - execute command with parameters here

        self.state = TaskState.COMPLETE

    @property
    def is_done(self):
        return self.state == TaskState.COMPLETE