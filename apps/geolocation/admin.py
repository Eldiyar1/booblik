from django.contrib import admin
from .models import Location, OperatingHours


class OperatingHoursInline(admin.TabularInline):
    model = OperatingHours
    extra = 6


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone_number')
    search_fields = ('address', 'phone_number')
    list_filter = ('address',)
    fieldsets = [
        ('Русский перевод', {
            'fields': ['address', 'phone_number', 'whatsapp_number', 'latitude', 'longitude', 'logo']
        })
        , ('Кыргызский перевод', {
            'fields': ['address_ky', 'phone_number_ky', 'whatsapp_number_ky', 'latitude_ky', 'longitude_ky', 'logo_ky']
        })
        , ('Английский перевод', {
            'fields': ['address_en', 'phone_number_en', 'whatsapp_number_en', 'latitude_en', 'longitude_en', 'logo_en']
        })
    ]

    inlines = [OperatingHoursInline]
