from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .models import Agent, Event
from .serializers import AgentSerializer, EventSerializer


class AgentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows agents to be viewed or edited.
    """

    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["environment", "status"]


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows events to be viewed or edited.
    """

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["level", "shelved"]
