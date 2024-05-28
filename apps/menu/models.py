from django.db import models

from apps.menu.constants import UnitChoices


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
    volume = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Объем")
    unit = models.CharField(max_length=2, choices=UnitChoices.choices(), verbose_name="Единицы измерения объема")
    menu = models.ForeignKey(Menu, models.CASCADE, related_name="products", verbose_name="Меню")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
