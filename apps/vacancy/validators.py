from rest_framework import serializers


def validate_file_size(value):
    max_size = 5 * 1024 * 1024
    if value.size > max_size:
        raise serializers.ValidationError('Размер файла слишком велик. Размер файла не должен превышать 5 МБ.')
