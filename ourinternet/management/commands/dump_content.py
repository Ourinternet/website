from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Stores content data.'

    def handle(self, **options):
        with open('commission/fixtures/partners.json', 'w') as f:
            call_command('dumpdata', 'commission.Partner', indent=2, stdout=f)

        with open('commission/fixtures/supporters.json', 'w') as f:
            call_command('dumpdata', 'commission.Supporter', indent=2, stdout=f)

        with open('commission/fixtures/members.json', 'w') as f:
            call_command('dumpdata', 'commission.Member', stdout=f)

        with open('commission/fixtures/media_contacts.json', 'w') as f:
            call_command('dumpdata', 'commission.MediaContact', indent=2, stdout=f)

        with open('commission/fixtures/press_release_footers.json', 'w') as f:
            call_command('dumpdata', 'commission.PressReleaseFooter', indent=2, stdout=f)

        with open('commission/fixtures/press_releases.json', 'w') as f:
            call_command('dumpdata', 'commission.PressRelease', indent=2, stdout=f)

        with open('commission/fixtures/events.json', 'w') as f:
            call_command('dumpdata', 'commission.Event', indent=2, stdout=f)

        with open('commission/fixtures/authors.json', 'w') as f:
            call_command('dumpdata', 'commission.Author', indent=2, stdout=f)

        with open('commission/fixtures/publication_types.json', 'w') as f:
            call_command('dumpdata', 'commission.PublicationType', indent=2, stdout=f)

        with open('commission/fixtures/publications.json', 'w') as f:
            call_command('dumpdata', 'commission.Publication', indent=2, stdout=f)

        with open('commission/fixtures/publication_authors.json', 'w') as f:
            call_command('dumpdata', 'commission.PublicationAuthor', indent=2, stdout=f)

        with open('commission/fixtures/faqs.json', 'w') as f:
            call_command('dumpdata', 'commission.FAQ', stdout=f)

        with open('structure/fixtures/sites.json', 'w') as f:
            call_command('dumpdata', 'sites', stdout=f)

        with open('structure/fixtures/pages.json', 'w') as f:
            call_command('dumpdata', 'flatpages', stdout=f)
