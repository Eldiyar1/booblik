from rest_framework import generics
from .models import Filial, Contact, Music, Image, AboutMe, AboutMeFact
from .serializers import FilialSerializer, ContactSerializer, MusicSerializer, ImageSerializer, AboutMeSerializer, \
    AboutMeFactSerializer


class FilialListAPIView(generics.ListAPIView):
    queryset = Filial.objects.all()
    serializer_class = FilialSerializer


class FilialRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Filial.objects.all()
    serializer_class = FilialSerializer


class ContactListAPIView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class MusicListAPIView(generics.ListAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer


class ImageListAPIView(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class AboutMeListAPIView(generics.ListAPIView):
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializer


class AboutMeFactListAPIView(generics.ListAPIView):
    queryset = AboutMeFact.objects.all()
    serializer_class = AboutMeFactSerializer
