from rest_framework import serializers

from .models import Agent, Event


class AgentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Agent
        fields = ["id", "url", "name", "status", "environment", "version", "address"]


class EventSerializer(serializers.HyperlinkedModelSerializer):
    agent_id = serializers.UUIDField()
    user_id = serializers.UUIDField()

    class Meta:
        model = Event
        fields = ["id", "url", "level", "message", "shelved", "date", "number_of_occurrences",
                  "agent_id", "user_id"]
