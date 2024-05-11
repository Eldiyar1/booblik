from django.db import models
from django.utils import timezone


class Menu(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='products/%Y/%m/%d/', verbose_name="Изображение")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    promotional_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,
                                            verbose_name="Акционная цена")
    promotion_start_date = models.DateField(null=True, blank=True, verbose_name="Дата начала акции")
    promotion_end_date = models.DateField(null=True, blank=True, verbose_name="Дата окончания акции")
    recommended = models.BooleanField(default=False, verbose_name="Рекомендуемый")
    liters = models.FloatField(null=True, blank=True, verbose_name="Литры",
                               help_text="Это поле предназначено только для напитков.")
    menu = models.ForeignKey(Menu, models.CASCADE, related_name="products", verbose_name="Меню")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    @property
    def current_price(self):
        """Возвращает актуальную цену продукта с учетом акций."""
        if self.promotional_price and self.promotion_start_date and self.promotion_end_date:
            now = timezone.now().date()
            if self.promotion_start_date <= now <= self.promotion_end_date:
                return self.promotional_price
        return self.price
