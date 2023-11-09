from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .models import Todo
from .serializers import TodoSerializer
from .permissions import IsOwner


class TodoViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing todos.
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'is_completed']
    search_fields = ['title', 'content']
    ordering_fields = ['updated_at']

    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        print(self.request)
        return Todo.objects.filter(user=self.request.user)
