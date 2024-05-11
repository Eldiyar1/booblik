from django.db import models
from django_summernote.fields import SummernoteTextField
from apps.filial.models import Filial


class Vacancy(models.Model):
    title = models.CharField(max_length=255, verbose_name="Должность")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    address = models.ForeignKey(Filial, on_delete=models.CASCADE, verbose_name="Адресс")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    requirements = SummernoteTextField(null=True, blank=True, verbose_name='Требования')

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"

    def __str__(self):
        return self.title
