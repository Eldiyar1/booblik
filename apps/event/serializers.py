from rest_framework import serializers
from .models import Event, News


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'media_file', 'publish_at', 'removal_at', 'is_published')


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'description')
