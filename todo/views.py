from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing todos.
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
