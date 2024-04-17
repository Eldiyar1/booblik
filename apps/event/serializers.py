from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'event_type', 'image', 'title', 'content', 'publish_at', 'removal_at', 'is_published')
