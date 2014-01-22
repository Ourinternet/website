from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Stores content data.'

    def handle(self, **options):
        with open('commission/fixtures/partners.json', 'w') as f:
            call_command('dumpdata', 'commission.Partner', indent=2, stdout=f)

        with open('commission/fixtures/members.json', 'w') as f:
            call_command('dumpdata', 'commission.Member', stdout=f)

        with open('commission/fixtures/faqs.json', 'w') as f:
            call_command('dumpdata', 'commission.FAQ', stdout=f)

        with open('structure/fixtures/sites.json', 'w') as f:
            call_command('dumpdata', 'sites', stdout=f)

        with open('structure/fixtures/pages.json', 'w') as f:
            call_command('dumpdata', 'flatpages', stdout=f)
