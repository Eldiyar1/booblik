from django.contrib import admin
from .models import Location, OperatingHours, Contact


class OperatingHoursInline(admin.TabularInline):
    model = OperatingHours
    extra = 6


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone_number')
    search_fields = ('address', 'phone_number')
    list_filter = ('address',)
    inlines = [OperatingHoursInline]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('whatsapp',)
