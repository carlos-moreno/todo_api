from rest_framework import viewsets

from .models import Todo
from .serializers import TodoSerializers


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



