# В файле populate_menus.py
from django.core.management.base import BaseCommand
from apps.menu.factories import MenuFactory

class Command(BaseCommand):
    help = 'Populates the Menu model with fake data'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Indicates the number of menus to be created')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        for _ in range(count):
            MenuFactory.create()
        self.stdout.write(self.style.SUCCESS(f'Successfully created {count} menu items'))
