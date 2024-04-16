from .models import Location, OperatingHours
from rest_framework import serializers


class OperatingHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperatingHours
        fields = ('day', 'open_time', 'close_time')


class LocationSerializer(serializers.ModelSerializer):
    operating_hours = OperatingHoursSerializer(many=True, read_only=True)

    class Meta:
        model = Location
        fields = (
            'id', 'logo', 'address', 'phone_number', 'whatsapp_number', 'operating_hours', 'latitude', 'longitude'
        )
