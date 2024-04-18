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
        }),
        ('Кыргызский перевод', {
            'fields': ['address_ky']
        }),
        ('Английский перевод', {
            'fields': ['address_en']
        })
    ]

    inlines = [OperatingHoursInline]
