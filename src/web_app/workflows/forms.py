from django.forms import ModelForm

from .models import WorkflowModel


class WorkflowForm(ModelForm):
    class Meta:
        model = WorkflowModel
        fields = '__all__'
