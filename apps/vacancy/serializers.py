from django.core.validators import FileExtensionValidator, MaxLengthValidator
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers
from .models import Vacancy
from ..common.serializers import BaseSerializer


class VacancyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('id', 'title')


class VacancyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('id', 'title', 'description', 'phone_number', 'address')


class ResumeSerializer(BaseSerializer):
    full_name = serializers.CharField(max_length=255)
    email = serializers.EmailField(required=False)
    phone_number = PhoneNumberField()
    resume = serializers.FileField(validators=[
        FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx']),
        MaxLengthValidator(5 * 1024 * 1024, message="Resume file is too large.")
    ])
