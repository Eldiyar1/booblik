from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from apps.geolocation.constants import DAY_CHOICES


class Location(models.Model):
    logo = models.ImageField(upload_to='logos/', verbose_name="Логотип")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    phone_number = PhoneNumberField(verbose_name="Номер телефона")
    whatsapp_number = models.URLField(verbose_name="Ссылка на WhatsApp")
    latitude = models.FloatField(null=True, blank=True, verbose_name="Широта")
    longitude = models.FloatField(null=True, blank=True, verbose_name="Долгота")

    class Meta:
        verbose_name = "Местоположение"
        verbose_name_plural = "Местоположения"

    def __str__(self):
        return self.address


class OperatingHours(models.Model):
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name='operating_hours',
        verbose_name="Местоположение"
    )
    day = models.CharField(max_length=10, choices=DAY_CHOICES, verbose_name="День недели")
    open_time = models.TimeField(verbose_name="Время открытия")
    close_time = models.TimeField(verbose_name="Время закрытия")

    class Meta:
        verbose_name = "Часы работы"
        verbose_name_plural = "Часы работы"
