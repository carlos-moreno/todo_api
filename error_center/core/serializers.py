from rest_framework import serializers

from .models import Agent, Event


class AgentSerializer(
    serializers.HyperlinkedModelSerializer, serializers.ModelSerializer
):
    class Meta:
        model = Agent
        fields = ["url", "name", "status", "environment", "version", "address"]


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ["url", "level", "message", "shelved", "date", "number_of_occurrences",
                  "agent", "user"]
