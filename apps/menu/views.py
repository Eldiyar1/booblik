from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer


class ProductsListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class RecommendedProductsListAPIView(generics.ListAPIView):
    queryset = Product.objects.filter(recommended=True)
    serializer_class = ProductSerializer


class NewProductsListAPIView(generics.ListAPIView):
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer


class ProductsByMenuAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        menu_id = self.kwargs['menu_id']
        return Product.objects.filter(menu_id=menu_id)


class BreakfastMenuProductsAPIView(generics.ListAPIView):
    queryset = Product.objects.filter(menu__name="Завтраки")
    serializer_class = ProductSerializer
