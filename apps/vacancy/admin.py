from django.contrib import admin
from .models import Vacancy


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'phone_number', 'address')
    list_filter = ('address',)
    search_fields = ('title', 'description', 'address')
