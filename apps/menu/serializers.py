from rest_framework import serializers
from .models import Menu, Product


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'name')


class ProductSerializer(serializers.ModelSerializer):
    menu = MenuSerializer()

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'image', 'price', 'recommended', 'menu')
