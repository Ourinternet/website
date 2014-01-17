from django.core.management.base import BaseCommand, CommandError
from tweet_cache.utils import get_tweets


class Command(BaseCommand):
    help = 'Loads tweets from the Twitter api and caches them.'

    def handle(self, **options):
         get_tweets()