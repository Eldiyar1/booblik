from django.db import models
from django_summernote.fields import SummernoteTextField
from apps.filial.models import Filial


class Vacancy(models.Model):
    title = models.CharField(max_length=255, verbose_name="Должность")
    description = models.TextField(verbose_name="Описание")
    address = models.ForeignKey(Filial, on_delete=models.CASCADE, verbose_name="Адресс")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"

    def __str__(self):
        return self.title


class Duties(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    title = SummernoteTextField(max_length=255, verbose_name='Обязанности')
    title_kgz = SummernoteTextField(max_length=255, verbose_name="Обязанности (KGZ)")
    title_en = SummernoteTextField(max_length=255, verbose_name="Обязанности (EN)")

    class Meta:
        verbose_name = 'Обязанности'
        verbose_name_plural = 'Обязанности'

    def __str__(self):
        return self.title


class Requirements(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    title = SummernoteTextField(max_length=255, verbose_name='Требования')
    title_kgz = SummernoteTextField(max_length=255, verbose_name="Требования (KGZ)")
    title_en = SummernoteTextField(max_length=255, verbose_name="Требования (EN)")

    class Meta:
        verbose_name = 'Требования'
        verbose_name_plural = 'Требования'

    def __str__(self):
        return self.title


class Conditions(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    title = SummernoteTextField(max_length=255, verbose_name='Условия')
    title_kgz = SummernoteTextField(max_length=255, verbose_name="Условия (KGZ)")
    title_en = SummernoteTextField(max_length=255, verbose_name="Условия (EN)")

    class Meta:
        verbose_name = 'Условия'
        verbose_name_plural = 'Условия'

    def __str__(self):
        return self.title
