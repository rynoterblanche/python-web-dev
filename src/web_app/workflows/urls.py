from django.urls import path

from django_web_app.views import ViewWrapper
from workflows import views
from workflows.factories import create_workflows_view, create_workflow_detail_view

# path('<int:id>', views.detail, name="detail"),

urlpatterns = [
    path('', ViewWrapper.as_view(view_creator_func=create_workflows_view), name="workflows"),
    path('<int:id>', ViewWrapper.as_view(view_creator_func=create_workflow_detail_view), name="detail"),
    path('tasks', views.tasks_list, name="tasks"),
    path('new', views.new, name="new"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('delete/<int:id>', views.delete, name="delete")
]
