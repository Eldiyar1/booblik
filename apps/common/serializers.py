from rest_framework import serializers


class BaseSerializer(serializers.Serializer):
    """
    Базовый сериализатор для обработки PhoneNumber.
    """
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if 'phone_number' in data:
            data['phone_number'] = str(instance.phone_number)
        return data
