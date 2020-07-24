import django_filters.rest_framework
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from todo.permissions import IsOwnerOrReadOnly
from .models import Todo
from .serializers import TodoSerializers


class TodoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)

    queryset = Todo.objects.all()
    serializer_class = TodoSerializers

    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,
                       filters.SearchFilter,
                       filters.OrderingFilter)
    filter_fields = ('name', 'done',)
    search_fields = ('name', 'description')
    ordering_fields = ('created_at', 'finished_in', 'done')

    def get_queryset(self):
        queryset = self.queryset
        result = queryset.filter(user=self.request.user)
        return result

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
