from django.forms import ModelForm

from workflows.models import Workflow


class WorkflowForm(ModelForm):
    class Meta:
        model = Workflow
        fields = '__all__'
