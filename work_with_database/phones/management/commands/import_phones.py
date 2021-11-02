import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            Phone.id = phone['id']
            Phone.name = phone['name']
            Phone.image = phone['image']
            Phone.price = phone['price']
            Phone.release_date = phone['release_date']
            Phone.lte_exists = phone['lte_exists']
        Phone.save()
