from django.core.management.base import BaseCommand
from django.core.management import call_command
from pathlib import Path

class Command(BaseCommand):
    help = "Загружает фикстуру moderators_group.json из users/fixtures/"

    def handle(self, *args, **options):
        app_dir = Path(__file__).resolve().parent.parent.parent
        fixtures_dir = app_dir / "fixtures"
        fixture_file = fixtures_dir / "moderators_with_users.json"

        if not fixture_file.exists():
            self.stderr.write(
                self.style.ERROR(
                    f"Фикстура не найдена: {fixture_file}"
                )
            )
            return

        self.stdout.write(self.style.SUCCESS(f"Начинаем загрузку фикстуры: {fixture_file}"))

        try:
            call_command("loaddata", str(fixture_file))
            self.stdout.write(self.style.SUCCESS("Фикстура успешно загружена."))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Ошибка при загрузке фикстуры: {e}"))
            raise
