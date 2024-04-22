from modeltranslation.translator import register, TranslationOptions
from .models import Event


@register(Event)
class EventTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'event_type', 'image', 'publish_at', 'removal_at', 'is_published')
