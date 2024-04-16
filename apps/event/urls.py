from django.urls import path
from apps.event.views import EventListAPIView

urlpatterns = [
    path('events/', EventListAPIView.as_view(), name='event-list'),
]
