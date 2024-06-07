import factory
from faker import Faker
from .models import Menu

fake = Faker('ru_RU')  # Используем русский язык для генерации данных


class MenuFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Menu

    name = factory.LazyAttribute(lambda _: fake.word())
