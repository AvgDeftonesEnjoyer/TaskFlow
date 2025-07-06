from django.contrib import admin
from django.urls import path, include
from .views import task_list_view, create_task, update_task, delete_task
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_views = get_schema_view(
    openapi.Info(
        title = 'TaskFlow Api',
        default_version = 'v1',
        description = 'TaskFlow API documentation',
    ),
    public = True,
    permission_classes = [permissions.AllowAny],
)

urlpatterns = [
    path('tasks/html/', task_list_view, name = 'task_list_view'),
    path('tasks/create/', create_task, name='create_task'),
    path('tasks/<int:pk>/edit/', update_task, name='update_task'),
    path('tasks/<int:pk>/delete/', delete_task, name='delete_task'),
    path('swagger/', schema_views.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_views.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]