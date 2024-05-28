from .models import Filial, Contact, Music, Image, AboutMe, AboutMeFact
from rest_framework import serializers


class FilialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filial
        fields = (
            'id', 'image', 'address', 'phone_number', 'whatsapp_number',
            'latitude', 'longitude', 'kitchen_closes', 'weekday_opening_time',
            'weekday_closing_time', 'sunday_opening_time', 'sunday_closing_time'
        )


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'whatsapp_number')


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id', 'audio_file')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'file')


class AboutMeSerializer(serializers.ModelSerializer):
    image = ImageSerializer()

    class Meta:
        model = AboutMe
        fields = ('id', 'image', 'title', 'description')


class AboutMeFactSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutMeFact
        fields = ('id', 'logo', 'description')
