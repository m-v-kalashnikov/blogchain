from django.core.management import BaseCommand

from core.fixtures.factories import CommentFactory, RateOfCommentFactory


class Command(BaseCommand):
    def handle(self, *args, **options):

        for _ in range(10):
            CommentFactory()

        for _ in range(20):
            RateOfCommentFactory()
