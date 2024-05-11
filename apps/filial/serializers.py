from .models import Filial, Contact
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
