from django.core.management import BaseCommand
from django.contrib.sites.models import Site
from os import environ as environment


class Command(BaseCommand):
    def handle(self, *args, **options):
        site = Site.objects.all()[0]
        site.domain = environment['DJANGO_DOMAIN']
        site.name = environment['DJANGO_NAME']
        site.save()
