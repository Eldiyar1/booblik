from django.urls import path
from .views import RecommendedProductsListAPIView, NewProductsListAPIView, ProductsListAPIView, ProductsByMenuAPIView

urlpatterns = [
    path('products/list/', ProductsListAPIView.as_view(), name='product_list'),
    path('products/new/', NewProductsListAPIView.as_view(), name='new_products'),
    path('products/recommended/', RecommendedProductsListAPIView.as_view(), name='recommended_products'),
    path('menu/<int:menu_id>/products/', ProductsByMenuAPIView.as_view(), name='products_by_menu'),
]
