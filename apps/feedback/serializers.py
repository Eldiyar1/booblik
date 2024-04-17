from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers
from apps.common.serializers import BaseSerializer


class FeedbackSerializer(BaseSerializer):
    full_name = serializers.CharField(max_length=255)
    phone_number = PhoneNumberField()
    comment = serializers.CharField(max_length=300, style={'base_template': 'textarea.html'})
