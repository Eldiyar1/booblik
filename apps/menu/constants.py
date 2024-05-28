from django.utils.translation import gettext_lazy as _
from django.utils.translation import get_language


class UnitChoices:
    GRAM = 'Гр'
    ML = 'Мл'
    LITRE = 'Л'

    @classmethod
    def choices(cls):
        return (
            (cls.GRAM, _("гр")),
            (cls.ML, _("мл")),
            (cls.LITRE, _("л")),
        )

    @classmethod
    def translate(cls):
        lang = get_language()
        translations = {
            'ru': {
                cls.GRAM: "гр",
                cls.ML: "мл",
                cls.LITRE: "л",
            },
            'ky': {
                cls.GRAM: "гр",
                cls.ML: "мл",
                cls.LITRE: "л",
            },
            'en': {
                cls.GRAM: "g",
                cls.ML: "ml",
                cls.LITRE: "L",
            }
        }
        return translations.get(lang, translations['ru'])
