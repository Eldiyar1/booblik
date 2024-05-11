from rest_framework import serializers
from .models import Menu, Product


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'name')


class ProductSerializer(serializers.ModelSerializer):
    menu = MenuSerializer()
    current_price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'image', 'price', 'promotional_price', 'promotion_start_date',
                  'promotion_end_date', 'current_price', 'recommended', 'liters', 'menu')

    @staticmethod
    def get_current_price(obj):
        return obj.current_price
