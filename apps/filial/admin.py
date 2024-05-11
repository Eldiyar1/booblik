from .models import Filial, Contact

from django.contrib import admin


@admin.register(Filial)
class FilialAdmin(admin.ModelAdmin):
    list_display = (
        'address', 'phone_number', 'whatsapp_number', 'kitchen_closes',
        'weekday_opening_time', 'weekday_closing_time',
        'sunday_opening_time', 'sunday_closing_time'
    )
    search_fields = ('address', 'phone_number', 'whatsapp_number')
    list_filter = ('address', 'kitchen_closes')

    fieldsets = (
        ("Основная информация",
         {'fields': ('image', 'address', 'phone_number', 'whatsapp_number', 'latitude', 'longitude')}),
        ("Время работы", {'fields': (
            'kitchen_closes', 'weekday_opening_time', 'weekday_closing_time',
            'sunday_opening_time', 'sunday_closing_time'
        )}),
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('whatsapp_number',)
