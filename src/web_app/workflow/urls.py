from django.urls import path

from src.web_app.workflow import views
from src.web_app.workflow.factories import create_workflows_view, create_workflow_detail_view
from src.web_app.django_web_app.views import ViewWrapper

urlpatterns = [
    path('', ViewWrapper.as_view(view_creator_func=create_workflows_view), name="workflow"),
    path('<int:id>', ViewWrapper.as_view(view_creator_func=create_workflow_detail_view), name="detail"),
    path('tasks', views.tasks_list, name="tasks"),
    path('new', views.new, name="new"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('delete/<int:id>', views.delete, name="delete")
]
