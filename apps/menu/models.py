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
    UNIT_CHOICES = (
        ('г', 'Гр'),
        ('мл', 'Мл'),
        ('л', 'Л'),
    )

    title = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='products/%Y/%m/%d/', verbose_name="Изображение")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    quantity = models.FloatField(null=True, blank=True, verbose_name="Количество")
    unit = models.CharField(max_length=2, choices=UNIT_CHOICES, verbose_name="Единицы измерения")
    menu = models.ForeignKey(Menu, models.CASCADE, related_name="products", verbose_name="Меню")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

