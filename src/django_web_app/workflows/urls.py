from django.urls import path

from workflows import views

urlpatterns = [
    path('<int:id>', views.detail, name="detail"),
    path('tasks', views.tasks_list, name="tasks"),
    path('new', views.new, name="new"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('delete/<int:id>', views.delete, name="delete")
]
