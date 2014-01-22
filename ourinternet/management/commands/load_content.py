from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Loads content data.'

    def handle(self, **options):
        call_command('loaddata', 'commission/fixtures/partners.json')
        call_command('loaddata', 'commission/fixtures/members.json')
        call_command('loaddata', 'commission/fixtures/faqs.json')
        call_command('loaddata', 'structure/fixtures/sites.json')
        call_command('loaddata', 'structure/fixtures/pages.json')
