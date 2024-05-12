from django.urls import path
from .views import ProductsListAPIView, ProductDetailAPIView, ProductsByMenuAPIView

urlpatterns = [
    path('products/list/', ProductsListAPIView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product_detail'),
    path('menu/<int:menu_id>/products/', ProductsByMenuAPIView.as_view(), name='products_by_menu'),
]
