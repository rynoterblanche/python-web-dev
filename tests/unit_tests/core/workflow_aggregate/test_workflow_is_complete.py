import unittest

from entities.workflow_aggregate.workflow import Workflow
from entities.workflow_aggregate.workflow_task import WorkflowTask, TaskState


class WorkflowIsComplete(unittest.TestCase):

    def setUp(self) -> None:
        task1 = WorkflowTask(1, "RunSql", {"sql": "select abc"})
        task2 = WorkflowTask(2, "CopyData", {"src": "gs://somefile", "dest": "/tmp/local"})
        self.tasks = [task1, task2]
        self.workflow = Workflow(1, "Wf1", self.tasks)

    def test_no_tasks_returns_false(self):
        workflow = Workflow(1, "Wf1", [])
        self.assertFalse(workflow.is_complete)

    def test_pending_tasks_returns_false(self):
        self.assertFalse(self.workflow.is_complete)

    def test_running_tasks_returns_false(self):
        for task in self.tasks:
            task.state = TaskState.RUNNING

        self.assertFalse(self.workflow.is_complete)

    def test_partially_complete_tasks_returns_false(self):
        self.tasks[0].state = TaskState.COMPLETE

        self.assertFalse(self.workflow.is_complete)

    def test_complete_tasks_returns_false(self):
        for task in self.tasks:
            task.state = TaskState.COMPLETE

        self.assertTrue(self.workflow.is_complete)
