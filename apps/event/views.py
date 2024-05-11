from rest_framework import generics
from .models import Event, News
from .serializers import EventSerializer, NewsSerializer


class EventListAPIView(generics.ListAPIView):
    queryset = Event.objects.filter(is_published=True).order_by('-publish_at')
    serializer_class = EventSerializer


class NewsListAPIView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsDetailAPIView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
