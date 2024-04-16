from django.urls import path
from .views import LocationListAPIView, LocationRetrieveAPIView

urlpatterns = [
    path("locations/", LocationListAPIView.as_view(), name="location-list-create"),
    path("locations/<int:pk>/", LocationRetrieveAPIView.as_view(), name="location-detail",),
]
