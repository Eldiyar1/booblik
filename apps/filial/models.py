from django.core.validators import FileExtensionValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Filial(models.Model):
    image = models.ImageField(
        upload_to='filial/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
        verbose_name="Изображение", )
    address = models.CharField(max_length=255, verbose_name="Адрес")
    phone_number = PhoneNumberField(verbose_name="Номер телефона")
    whatsapp_number = PhoneNumberField(verbose_name="Номер WhatsApp")
    kitchen_closes = models.TimeField(verbose_name="Кухня работает до")
    weekday_opening_time = models.TimeField(verbose_name="Открытие по будням")
    weekday_closing_time = models.TimeField(verbose_name="Закрытие по будням")
    sunday_opening_time = models.TimeField(verbose_name="Открытие в воскресенье")
    sunday_closing_time = models.TimeField(verbose_name="Закрытие в воскресенье")
    latitude = models.FloatField(verbose_name="Широта")
    longitude = models.FloatField(verbose_name="Долгота")

    class Meta:
        verbose_name = "Филиал"
        verbose_name_plural = "Филиалы"

    def __str__(self):
        return self.address


class Contact(models.Model):
    whatsapp_number = PhoneNumberField(null=True, verbose_name="Номер WhatsApp")

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return f'Номер WhatsApp {self.whatsapp_number}'
