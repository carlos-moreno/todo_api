from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from .api_policies import OnlyAdminCreate
from .models import Agent, Event
from .serializers import AgentSerializer, EventSerializer


class AgentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows agents to be viewed or edited.
    """

    authentication_classes = [TokenAuthentication]
    permission_classes = [OnlyAdminCreate]

    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["environment", "status"]
    search_fields = ['name', 'environment', 'version', 'address']


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows events to be viewed or edited.
    """

    authentication_classes = [TokenAuthentication]
    permission_classes = [OnlyAdminCreate]

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["level", "date"]
    search_fields = ['level', 'message']
    ordering_fields = ['level', 'date']
