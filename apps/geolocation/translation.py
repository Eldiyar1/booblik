from modeltranslation.translator import register, TranslationOptions
from .models import Location

@register(Location)
class LocationTranslationOptions(TranslationOptions):
    fields = ('address', 'phone_number', 'whatsapp_number', 'latitude', 'longitude','logo')
