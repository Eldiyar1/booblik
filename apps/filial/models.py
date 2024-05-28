from django.core.validators import FileExtensionValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.validators import validate_file_size, validate_svg_dimensions


class Filial(models.Model):
    image = models.ImageField(
        upload_to='filial/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
        verbose_name="Изображение"
    )
    address = models.CharField(max_length=255, verbose_name="Адрес")
    phone_number = PhoneNumberField(verbose_name="Номер телефона")
    whatsapp_number = PhoneNumberField(verbose_name="Номер WhatsApp")
    kitchen_closes = models.TimeField(verbose_name="Кухня работает до")
    weekday_opening_time = models.TimeField(verbose_name="Пн-Сб открытие")
    weekday_closing_time = models.TimeField(verbose_name="Пн-Сб закрытие")
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


class Music(models.Model):
    audio_file = models.FileField(upload_to='music/', null=True, blank=True, verbose_name='Аудио файл',
                                  validators=[
                                      FileExtensionValidator(allowed_extensions=['mp3', 'wav', 'ogg', 'flac', 'aac']),
                                      validate_file_size
                                  ],
                                  help_text="Разрешенные форматы аудио-файлов: mp3, wav, ogg, flac, aac")

    class Meta:
        verbose_name = 'Музыка'
        verbose_name_plural = 'Музыка'

    def __str__(self):
        return f'{self.audio_file.name}'


class Image(models.Model):
    file = models.ImageField(
        upload_to='images/about_me/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
        verbose_name="Файл изображения"
    )

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображение'


class AboutMe(models.Model):
    image = models.ImageField(
        upload_to='filial/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
        verbose_name="Изображение"
    )
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = 'Обо мне'
        verbose_name_plural = 'Обо мне'

    def __str__(self):
        return self.title


class AboutMeFact(models.Model):
    logo = models.FileField(
        upload_to='about_me_facts/',
        validators=[FileExtensionValidator(['svg']), validate_svg_dimensions],
        verbose_name="Логотип"
    )
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = 'Факт обо мне'
        verbose_name_plural = 'Факты обо мне'
