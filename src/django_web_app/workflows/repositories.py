from workflows.models import Workflow


class WorkflowsRepo:

    def list(self):
        return Workflow.objects.all()
