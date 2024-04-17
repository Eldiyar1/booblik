from django.core.validators import FileExtensionValidator
from django.db import models
from apps.event.constants import EVENT_TYPES


class Event(models.Model):
    event_type = models.CharField(max_length=50, choices=EVENT_TYPES, verbose_name='Тип события')
    image = models.ImageField(
        upload_to='events/%Y/%m/%d/',
        verbose_name="Изображение",
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    publish_at = models.DateTimeField(verbose_name='Дата и время публикации')
    removal_at = models.DateTimeField(verbose_name='Дата и время удаления')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

    def __str__(self):
        return self.title
