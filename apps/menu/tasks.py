from django.utils import timezone
from celery import shared_task
from .models import Product


@shared_task
def update_product_prices():
    try:
        now = timezone.now().date()
        minutes_before_now = now - timezone.timedelta(minutes=3)  # Тест на продукты, акция которых закончилась в течение последних 5 минут
        products = Product.objects.filter(promotion_end_date__lte=minutes_before_now, promotional_price__isnull=False)
        for product in products:
            product.promotional_price = None
            product.promotion_start_date = None
            product.promotion_end_date = None
            product.save()
        return f"Обновлены цены для {products.count()} продуктов."
    except Exception as e:
        return f"Произошла ошибка: {str(e)}"

