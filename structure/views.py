from django.shortcuts import render, redirect
from random import randint
from django.conf import settings
import tweepy
from forms import ContactForm
from django.core.mail import EmailMessage
from django.contrib import messages
from django.contrib.flatpages.models import FlatPage

from commission.models import Member


def home(request, template="structure/home.html"):

    consumer_key = settings.TWITTER_CONSUMER_KEY
    consumer_secret = settings.TWITTER_CONSUMER_SECRET
    auth = tweepy.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)
    api = tweepy.API(auth)

    user = api.get_user(settings.TWITTER_USER)

    public_tweets = user.timeline()

    process_tweets(public_tweets)

    video_number = randint(1, 3)

    main_page = FlatPage.objects.get(url='/main/')
    about_page = FlatPage.objects.get(url='/about/')
    press_page = FlatPage.objects.get(url='/press/')
    partner_page = FlatPage.objects.get(url='/partner/')
    commission_page = FlatPage.objects.get(url='/commission/')
    event_page = FlatPage.objects.get(url='/event/')
    footer_page = FlatPage.objects.get(url='/footer/')
    contact_form = ContactForm()

    chair_members = list(Member.objects.filter(chair=True).order_by("last_name"))
    other_members = list(Member.objects.filter(chair=False).order_by("last_name"))

    context = {'public_tweets': public_tweets,
               'video_number': video_number,
               'main_page': main_page,
               'about_page': about_page,
               'press_page': press_page,
               'partner_page': partner_page,
               'commission_page': commission_page,
               'event_page': event_page,
               'footer_page': footer_page,
               'contact_form': contact_form,
               'chair_members': chair_members,
               'other_members': other_members,
               'GA_SITE_ID': settings.GA_SITE_ID,
               'GA_SITE_URL': settings.GA_SITE_URL,
               }

    return render(request, template, context)


def process_tweets(tweets):
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

        tweet.text = tweet_text


def contact_submit(request):
    #request.is_ajax() and
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            subject = "[OurInternet Contact Form] %s" % form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_sender = form.cleaned_data['cc_myself']

            recipients = settings.CONTACT_FORM_RECIPIENT_LIST

            cc_list = []
            if cc_sender:
                cc_list = [sender]

            email = EmailMessage(subject, message, from_email=sender, to=recipients, cc=cc_list)
            email.send()

            form = ContactForm()
            messages.add_message(request, messages.SUCCESS, 'Your email has been sent.')

        else:
            messages.add_message(request, messages.ERROR,
                                 'There has been an error submitting your form.')

        return render(request, 'structure/_contact.html', {'contact_form': form})
    else:
        form = ContactForm()

    return render(request, 'structure/_contact.html', {'contact_form': form})

