from rest_framework import serializers

from .models import Todo


class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ("id", "name", "description", "done", "created_at", "finished_in", "user")
        extra_kwargs = {
            "created_at": {"read_only": True},
            "finished_in": {"read_only": True},
            "user": {"read_only": True}
        }
