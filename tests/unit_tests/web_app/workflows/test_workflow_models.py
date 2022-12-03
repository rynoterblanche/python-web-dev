import os

from django.test import TestCase

from src.web_app.workflow.models import Workflow


class TestWorkflowModels(TestCase):

    def setUp(self) -> None:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.web_app.django_web_app.settings')

    def test_workflow_model_creation(self) -> None:
        model = Workflow(1, "Wf1")
        self.assertIsInstance(model, Workflow)
