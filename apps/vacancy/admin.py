from django.contrib import admin
from .models import Vacancy, Duties, Requirements, Conditions


class DutiesInline(admin.TabularInline):
    model = Duties
    max_num = 1


class RequirementsInline(admin.TabularInline):
    model = Requirements
    max_num = 1


class ConditionsInline(admin.TabularInline):
    model = Conditions
    max_num = 1


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'created_at')  # Добавляем 'created_at' в список отображаемых полей
    list_filter = ('address', 'title', 'created_at')
    search_fields = ('title', 'description', 'address')
    inlines = [DutiesInline, RequirementsInline, ConditionsInline]
    fieldsets = [
        ('Русский перевод', {
            'fields': ['title', 'description', 'address']
        }),
        ('Кыргызский перевод', {
            'fields': ['title_ky', 'description_ky']
        }),
        ('Английский перевод', {
            'fields': ['title_en', 'description_en']
        }),
    ]
