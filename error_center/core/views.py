
from rest_framework import viewsets

from .models import Agent, Event
from .serializers import AgentSerializer, EventSerializer


class AgentViewSet(viewsets.ModelViewSet):
    """Make doc here"""
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer


class EventViewSet(viewsets.ModelViewSet):
    """Make doc here"""
    queryset = Event.objects.all()
    serializer_class = EventSerializer
