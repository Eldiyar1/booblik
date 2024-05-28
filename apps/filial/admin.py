from .models import Filial, Contact, Music, Image, AboutMe, AboutMeFact
from django.contrib import admin

from ..common.mixins import LimitInstancesMixin


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


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ('id', 'audio_file')


@admin.register(Image)
class ImageAdmin(LimitInstancesMixin, admin.ModelAdmin):
    list_display = ('id', 'file')
    max_instances = 1
    instance_name = 'изображение'


@admin.register(AboutMe)
class AboutMeAdmin(LimitInstancesMixin, admin.ModelAdmin):
    list_display = ('title',)
    max_instances = 3
    instance_name = 'объекта "Обо мне"'
    fieldsets = [
        ('Русский перевод', {
            'fields': ['image', 'title', 'description']
        }),
        ('Кыргызский перевод', {
            'fields': ['title_ky', 'description_ky']
        }),
        ('Английский перевод', {
            'fields': ['title_en', 'description_en']
        })
    ]


@admin.register(AboutMeFact)
class AboutMeFactAdmin(LimitInstancesMixin, admin.ModelAdmin):
    list_display = ('id', 'logo', 'description')
    max_instances = 6
    instance_name = 'фактов обо мне'
    fieldsets = [
        ('Русский перевод', {
            'fields': ['logo', 'description']
        }),
        ('Кыргызский перевод', {
            'fields': ['description_ky']
        }),
        ('Английский перевод', {
            'fields': ['description_en']
        })
    ]
