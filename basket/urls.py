from django.urls import path
from . import views

urlpatterns = [
    path('create_task/', views.CreateTask.as_view(), name='create_task'),
    path('task_list/', views.TaskListView.as_view(), name='task_list'),
    path('task_list/<int:id>/', views.TaskDetailView.as_view(), name='task_detail'),
    path('task_list/<int:id>/update/', views.TaskUpdateView.as_view(), name='task_update'),
    path('task_list/<int:id>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
    path('search_basket/', views.SearchTaskView.as_view(), name='search_task'),
]