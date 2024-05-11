from django.urls import path
from apps.event.views import EventListAPIView, NewsListAPIView, NewsDetailAPIView

urlpatterns = [
    path('events/', EventListAPIView.as_view(), name='event-list'),
    path('news/', NewsListAPIView.as_view(), name='news-list'),
    path('news/<int:pk>/', NewsDetailAPIView.as_view(), name='news-detail'),
]
