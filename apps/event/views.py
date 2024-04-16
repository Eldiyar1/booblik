from rest_framework import generics
from .models import Event
from .serializers import EventSerializer


class EventListAPIView(generics.ListAPIView):
    queryset = Event.objects.filter(is_published=True).order_by('-publish_at')
    serializer_class = EventSerializer
