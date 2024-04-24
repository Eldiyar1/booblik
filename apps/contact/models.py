from django.db import models


class Contact(models.Model):
    whatsapp = models.URLField(verbose_name='WhatsApp ссылка')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return f'WhatsApp контакт {self.whatsapp}'
