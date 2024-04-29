from django.urls import path
from .views import LocationListAPIView, LocationRetrieveAPIView, ContactListAPIView

urlpatterns = [
    path("locations/", LocationListAPIView.as_view(), name="location-list-create"),
    path("locations/<int:pk>/", LocationRetrieveAPIView.as_view(), name="location-detail",),
    path('contacts/', ContactListAPIView.as_view(), name='contact-list'),
]
