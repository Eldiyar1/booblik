from django.contrib import admin
from .models import Vacancy


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'created_at')
    list_filter = ('address', 'title', 'created_at')
    search_fields = ('title', 'description', 'address')
    fieldsets = [
        ('Русский перевод', {
            'fields': ['title', 'address', 'requirements']
        }),
        ('Кыргызский перевод', {
            'fields': ['title_ky', 'requirements_ky']
        }),
        ('Английский перевод', {
            'fields': ['title_en', 'requirements_en']
        }),
    ]
