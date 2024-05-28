from django.contrib import admin
from django.utils.html import format_html

from .models import Event, News
from ..common.mixins import LimitInstancesMixin


def update_publish_status(modeladmin, request, queryset, status):
    queryset.update(is_published=status)


def publish_selected_events(modeladmin, request, queryset):
    update_publish_status(modeladmin, request, queryset, True)


def unpublish_selected_events(modeladmin, request, queryset):
    update_publish_status(modeladmin, request, queryset, False)


publish_selected_events.short_description = "Опубликовать выбранные события"
unpublish_selected_events.short_description = "Отменить публикацию выбранных событий"


@admin.register(Event)
class EventAdmin(LimitInstancesMixin, admin.ModelAdmin):
    list_display = ('id', 'media_preview', 'publish_at', 'removal_at', 'is_published')
    actions = (publish_selected_events, unpublish_selected_events)
    max_instances = 5
    instance_name = 'Событий'

    def media_preview(self, obj):
        if obj.media_file and obj.media_file.url.endswith(('jpg', 'jpeg', 'png')):
            return format_html('<img src="{}" style="max-width: 100px; max-height: 100px; object-fit: cover;">',
                               obj.media_file.url)
        elif obj.media_file and obj.media_file.url.endswith('pdf'):
            return format_html('<a href="{}" target="_blank">Просмотр PDF</a>', obj.media_file.url)
        return "Файл не поддерживается"

    media_preview.short_description = "Медиа файл"

    fieldsets = (
        (None, {'fields': ('media_file', 'publish_at', 'removal_at', 'is_published')}),
    )


@admin.register(News)
class NewsAdmin(LimitInstancesMixin, admin.ModelAdmin):
    list_display = ('id', 'image', 'title', 'description')
    max_instances = 4
    instance_name = 'Новости'
    fieldsets = [
        ('Русский перевод', {
            'fields': ['image', 'title', 'description', ]
        }),
        ('Кыргызский перевод', {
            'fields': ['title_ky', 'description_ky']
        }),
        ('Английский перевод', {
            'fields': ['title_en', 'description_en']
        }),
    ]
