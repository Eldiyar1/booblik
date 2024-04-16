from rest_framework import generics
from .models import Location
from .serializers import LocationSerializer


class LocationListAPIView(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
