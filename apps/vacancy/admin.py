from django.contrib import admin
from .models import Vacancy


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'phone_number', 'address')
    list_filter = ('address',)
    search_fields = ('title', 'description', 'address')
    fieldsets = [
        ('Русский перевод', {
            'fields': ['title', 'description', 'phone_number', 'address']
        }),
        ('Кыргызский перевод', {
            'fields': ['title_ky', 'description_ky', 'address_ky']
        }),
        ('Английский перевод', {
            'fields': ['title_en', 'description_en', 'address_en']
        }),
    ]

