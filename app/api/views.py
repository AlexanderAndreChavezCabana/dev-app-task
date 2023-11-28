from django.shortcuts import render
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema_view, extend_schema

# Create your views here.

from api.serializers import TaskSerializer
from api.models import Task

@extend_schema_view(
    list=extend_schema(description='Permite obtener una lista de tareas.'),
    retrieve=extend_schema(description='Permite obtener una tarea.'),
    create=extend_schema(description='Permite actualizar una tarea.'),
    update=extend_schema(description='Permite eliminar una tarea.'),
    destroy=extend_schema(description='Permite eliminar una tarea')
)

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()