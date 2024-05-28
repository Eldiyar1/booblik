from django.urls import path
from .views import ProductsListAPIView, ProductDetailAPIView

urlpatterns = [
    path('products/list/', ProductsListAPIView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product_detail'),
]
