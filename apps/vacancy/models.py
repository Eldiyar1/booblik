from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Vacancy(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    phone_number = PhoneNumberField(verbose_name="Номер телефона")
    address = models.CharField(max_length=255, verbose_name="Адрес")

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"

    def __str__(self):
        return self.title
