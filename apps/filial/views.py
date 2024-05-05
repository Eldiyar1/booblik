from rest_framework import generics
from .models import Filial, Contact
from .serializers import FilialSerializer, ContactSerializer


class FilialListAPIView(generics.ListAPIView):
    queryset = Filial.objects.all()
    serializer_class = FilialSerializer


class FilialRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Filial.objects.all()
    serializer_class = FilialSerializer


class ContactListAPIView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
