from django.conf import settings
import tweepy

from models import Tweet


def get_tweets():
    consumer_key = settings.TWITTER_CONSUMER_KEY
    consumer_secret = settings.TWITTER_CONSUMER_SECRET
    auth = tweepy.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)
    api = tweepy.API(auth)

    user = api.get_user(settings.TWITTER_USER)

    public_tweets = user.timeline()

    process_tweets(public_tweets, settings.TWITTER_USER)


def process_tweets(tweets, account):
    tweets = list(tweets)
    tweets.reverse()
    for tweet in tweets:
        tweet_text = tweet.text
        hashtags = tweet.entities["hashtags"]
        links = tweet.entities["urls"]
        user_mentions = tweet.entities["user_mentions"]
        symbols = tweet.entities["symbols"]

        for hashtag in hashtags:
            original_tag = "#%s" % hashtag['text']
            markup = "<a class='twitter-link hashtag' href='https://twitter.com%s'>%s</a>" % (original_tag,
                                                                                              original_tag)
            tweet_text = tweet_text.replace(original_tag, markup)

        for link in links:
            original_link = link['url']
            markup = "<a class='twitter-link' href='%s'>%s</a>" % (link['expanded_url'], original_link)
            tweet_text = tweet_text.replace(original_link, markup)

        for user_mention in user_mentions:
            original_mention = "@%s" % user_mention['screen_name']
            markup = "<a class='twitter-link user-mention' href='https://twitter.com/%s'>%s</a>" % (original_mention,
                                                                                                    original_mention)
            tweet_text = tweet_text.replace(original_mention, markup)

        cached_tweet, created = Tweet.objects.get_or_create(tweet_id=tweet.id,
                                                            defaults={
                                                                'account': account,
                                                                'profile_image_url':tweet.user.profile_image_url,
                                                                'text':tweet.text,
                                                                'processed_text':tweet_text,
                                                            })

        cached_tweet.save()