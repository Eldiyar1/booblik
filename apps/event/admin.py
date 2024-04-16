from django.contrib import admin
from .models import Event


def update_publish_status(modeladmin, request, queryset, status):
    queryset.update(is_published=status)


def publish_selected_events(modeladmin, request, queryset):
    update_publish_status(modeladmin, request, queryset, True)


def unpublish_selected_events(modeladmin, request, queryset):
    update_publish_status(modeladmin, request, queryset, False)


publish_selected_events.short_description = "Опубликовать выбранные события"
unpublish_selected_events.short_description = "Отменить публикацию выбранных событий"


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('event_type', 'title', 'publish_at', 'is_published')
    actions = (publish_selected_events, unpublish_selected_events)
    fieldsets = [
        ('Русский перевод', {
            'fields': ['event_type', 'title', 'content', 'image', 'publish_at', 'is_published']
        })
        , ('Кыргызский перевод', {
            'fields': ['event_type_ky', 'title_ky', 'content_ky', 'image_ky', 'publish_at_ky', 'is_published_ky']
        })
        , ('Английский перевод', {
            'fields': ['event_type_en', 'title_en', 'content_en', 'image_en', 'publish_at_en', 'is_published_en']
        })
    ]
