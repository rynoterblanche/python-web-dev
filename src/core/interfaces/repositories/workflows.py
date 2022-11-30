import abc
from typing import List

from src.core.entities.workflow_aggregate.workflow import Workflow


class WorkflowRepository(abc.ABC):

    @abc.abstractmethod
    def get_by_id(self, workflow_id: int) -> Workflow:
        raise NotImplementedError

    @abc.abstractmethod
    def list(self) -> List[Workflow]:
        raise NotImplementedError

