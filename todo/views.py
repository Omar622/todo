from rest_framework import viewsets
from .models import Todo


class TodoViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for viewing and editing todos.
    """
    queryset = Todo.objects.all()
    # serializer_class = AccountSerializer
