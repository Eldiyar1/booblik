from django.core.validators import FileExtensionValidator
from django.db import models


class Event(models.Model):
    media_file = models.FileField(
        upload_to='events/%Y/%m/%d/',
        verbose_name="Медиа файл",
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'pdf'])])
    publish_at = models.DateTimeField(verbose_name='Дата и время публикации')
    removal_at = models.DateTimeField(verbose_name='Дата и время удаления')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

    def __str__(self):
        return f'Событие от {self.publish_at.strftime("%H:%M %d-%m-%Y")}'
