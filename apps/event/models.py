from django.db import models
from django.core.validators import FileExtensionValidator


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


class News(models.Model):
    image = models.ImageField(
        upload_to='filial/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
        verbose_name="Изображение"
    )
    title = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
