from rest_framework import serializers

from .constants import UnitChoices
from .models import Menu, Product


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'name')


class ProductSerializer(serializers.ModelSerializer):
    menu = MenuSerializer()
    unit_display = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'image', 'price', 'volume', 'unit_display', 'menu')

    @staticmethod
    def get_unit_display(obj):
        return UnitChoices.translate().get(obj.unit)
