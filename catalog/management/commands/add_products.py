from django.core.management import call_command
from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Delite all data from the db and load test data from fixture"

    def handle(self, *args, **kwargs):
        # Удаляем существующие записи
        Category.objects.all().delete()
        Product.objects.all().delete()

        # Загрузка данных из фикстуры
        call_command("loaddata", "catalog/fixtures/category_fixtures.json")
        call_command("loaddata", "catalog/fixtures/product_fixtures.json")

        self.stdout.write(self.style.SUCCESS("Successfully loaded data from fixture"))
