from django.test import TestCase

from src.web_app.workflow.models import Workflow


class TestWorkflowModels(TestCase):

    def test_workflow_model_creation(self) -> None:
        model = Workflow(1, "Wf1")
        self.assertIsInstance(model, Workflow)
