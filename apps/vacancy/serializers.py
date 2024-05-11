from django.core.validators import FileExtensionValidator
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

from .models import Vacancy, Duties, Requirements, Conditions
from .validators import validate_file_size


class VacancyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('id', 'title')


class VacancyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('id', 'title', 'description', 'address')


class DutiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Duties
        fields = ('id', 'title')


class RequirementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirements
        fields = ('id', 'title')


class ConditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conditions
        fields = ('id', 'title')


class ResumeSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=50)
    phone_number = PhoneNumberField()
    birth_date = serializers.DateField(required=False, allow_null=True, input_formats=['%d.%m.%Y'])
    resume = serializers.FileField(
        validators=[
            FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx']),
            validate_file_size
        ]
    )
