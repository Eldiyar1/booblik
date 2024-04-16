from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='product_images/', verbose_name="Изображение")
    calories = models.FloatField(verbose_name="Калорийность")
    proteins = models.FloatField(verbose_name="Белки")
    fats = models.FloatField(verbose_name="Жиры")
    carbohydrates = models.FloatField(verbose_name="Углеводы")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    products = models.ForeignKey(Product, models.PROTECT, verbose_name="Продукты")

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"

    def __str__(self):
        return self.name
