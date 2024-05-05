from .models import Filial, OperatingHours, Contact
from rest_framework import serializers


class OperatingHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperatingHours
        fields = ('day', 'open_time', 'close_time')


class FilialSerializer(serializers.ModelSerializer):
    operating_hours = OperatingHoursSerializer(many=True, read_only=True)

    class Meta:
        model = Filial
        fields = (
            'id', 'logo', 'address', 'phone_number', 'whatsapp_number', 'operating_hours', 'latitude', 'longitude'
        )


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'whatsapp')
