from modeltranslation.translator import register, TranslationOptions
from .models import AboutMe, AboutMeFact


@register(AboutMe)
class AboutMeTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(AboutMeFact)
class AboutMeFactTranslationOptions(TranslationOptions):
    fields = ('description',)
