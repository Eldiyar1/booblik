from rest_framework import generics
from .models import Location, Contact
from .serializers import LocationSerializer, ContactSerializer


class LocationListAPIView(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class ContactListAPIView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer