import os
import shutil
import tempfile
import xml.etree.ElementTree as ET
from django.core.exceptions import ValidationError
from rest_framework import serializers


def validate_file_size(value):
    max_size = 5 * 1024 * 1024
    if value.size > max_size:
        raise serializers.ValidationError('Размер файла слишком велик. Размер файла не должен превышать 5 МБ.')


def validate_svg_dimensions(value):
    try:
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            shutil.copyfileobj(value, tmp_file)

        with open(tmp_file.name, 'rb') as f:
            svg_content = f.read()

        root = ET.fromstring(svg_content)
        width_str = root.attrib.get('width', '')
        height_str = root.attrib.get('height', '')

        if width_str.endswith(('px', 'pt', 'em', 'rem')):
            width = float(width_str[:-2])
        else:
            width = float(width_str)

        if height_str.endswith(('px', 'pt', 'em', 'rem')):
            height = float(height_str[:-2])
        else:
            height = float(height_str)

        if abs(width - 40) > 2 or abs(height - 40) > 2:
            raise ValidationError("Размеры SVG файла должны быть примерно 40x40 пикселей.")
    except (ET.ParseError, AttributeError, ValueError) as e:
        raise ValidationError("Невозможно прочитать размеры SVG файла: %(error)s", params={'error': str(e)})
    finally:
        os.unlink(tmp_file.name)
