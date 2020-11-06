from django.core.management import BaseCommand

from core.fixtures.factories import UserFactory


class Command(BaseCommand):
    def handle(self, *args, **options):

        for _ in range(5):
            UserFactory()
