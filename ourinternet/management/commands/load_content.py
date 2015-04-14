from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Loads content data.'

    def handle(self, **options):
        call_command('loaddata', 'commission/fixtures/partners.json')
        call_command('loaddata', 'commission/fixtures/supporters.json')
        call_command('loaddata', 'commission/fixtures/members.json')
        call_command('loaddata', 'commission/fixtures/media_contacts.json')
        call_command('loaddata', 'commission/fixtures/press_release_footers.json')
        call_command('loaddata', 'commission/fixtures/press_releases.json')
        call_command('loaddata', 'commission/fixtures/events.json')
        call_command('loaddata', 'commission/fixtures/authors.json')
        call_command('loaddata', 'commission/fixtures/publication_types.json')
        call_command('loaddata', 'commission/fixtures/publications.json')
        call_command('loaddata', 'commission/fixtures/publication_authors.json')
        call_command('loaddata', 'commission/fixtures/faqs.json')
        call_command('loaddata', 'commission/fixtures/videos.json')
        call_command('loaddata', 'structure/fixtures/sites.json')
        call_command('loaddata', 'structure/fixtures/pages.json')
        call_command('loaddata', 'structure/fixtures/aliases.json')
