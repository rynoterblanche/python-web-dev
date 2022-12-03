from django.forms import ModelForm

from src.web_app.workflow.models import Workflow


class WorkflowForm(ModelForm):
    class Meta:
        model = Workflow
        fields = '__all__'
