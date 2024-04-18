from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers
from apps.geolocation.models import Location


class FeedbackSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=255)
    phone_number = PhoneNumberField()
    comment = serializers.CharField(max_length=300, style={'base_template': 'textarea.html'})
    location_id = serializers.PrimaryKeyRelatedField(queryset=Location.objects.only('id'), write_only=True)
