from django.core.validators import FileExtensionValidator
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

from .constants import GENDER_CHOICES
from .models import Vacancy
from .validators import validate_file_size


class VacancyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('id', 'title')


class VacancyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('id', 'title', 'description', 'phone_number', 'address')


class ResumeSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=255)
    phone_number = PhoneNumberField()
    birth_date = serializers.DateField(required=False, allow_null=True, input_formats=['%d.%m.%Y'])
    email = serializers.EmailField(required=False, allow_null=True)
    gender = serializers.ChoiceField(choices=GENDER_CHOICES, required=False, allow_null=True)
    resume = serializers.FileField(
        validators=[
            FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx']),
            validate_file_size
        ]
    )
