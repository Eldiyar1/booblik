from modeltranslation.translator import register, TranslationOptions
from .models import Menu, Product


@register(Menu)
class MenuTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'calories', 'proteins', 'fats', 'carbohydrates')
