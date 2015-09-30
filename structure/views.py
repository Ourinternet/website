from django.shortcuts import render, redirect, get_object_or_404
from random import randint
from django.conf import settings
from forms import ContactForm
from django.core.mail import EmailMessage
from django.contrib import messages
from django.contrib.flatpages.models import FlatPage
from django.views.generic import RedirectView
from tweet_cache.models import Tweet
from commission.models import Member, FAQ, PressRelease, Partner, Supporter, \
    MediaContact, Event, Publication, Video, Feature
from .models import UrlAlias
from datetime import datetime
import pytz


def home(request, template="structure/home.html"):

    public_tweets = Tweet.objects.filter(account=settings.TWITTER_USER, hide=False).order_by("-id")[:20]

    video_number = randint(1, 3)

    main_page, created = FlatPage.objects.get_or_create(url='/main/')
    about_page, created = FlatPage.objects.get_or_create(url='/about/')
    # press_page, created = FlatPage.objects.get_or_create(url='/press/')
    # partner_page, created = FlatPage.objects.get_or_create(url='/partner/')
    commission_page, created = FlatPage.objects.get_or_create(url='/commission/')
    event_page, created = FlatPage.objects.get_or_create(url='/event/')
    footer_page, created = FlatPage.objects.get_or_create(url='/footer/')
    contact_page, created = FlatPage.objects.get_or_create(url='/contact/')
    research_advisers_page, created = FlatPage.objects.get_or_create(url='/research_advisers/')
    contact_form = ContactForm()

    faq_page, created = FlatPage.objects.get_or_create(url='/faq/')
    faq_list = FAQ.objects.all().order_by('weight')

    chair_members = list(Member.objects.filter(member_type="chair").order_by("last_name"))
    other_members = list(Member.objects.filter(member_type="general").order_by("last_name"))
    supporting_members = list(Member.objects.filter(member_type="supporting").order_by("last_name"))

    research_advisers = list(Member.objects.filter(member_type="research_adviser").order_by("last_name"))

    press_releases = PressRelease.objects.all().order_by("-release_date")
    partners = Partner.objects.all().order_by("weight")
    supporters = Supporter.objects.all().order_by("weight")
    media_contacts = MediaContact.objects.filter(display_on_contact=True).order_by("weight")

    today = datetime.now(tz=pytz.timezone(settings.SERVER_TIMEZONE)).replace(tzinfo=pytz.timezone("UTC"))
    current_events = Event.objects.filter(end_date__gte=today).order_by("start_date")
    past_events = Event.objects.filter(end_date__lt=today).order_by("-start_date")

    publications = Publication.objects.all().order_by("-publish_date", "weight")

    videos = Video.objects.all().order_by("weight")

    features = Feature.objects.filter(disable=False).order_by("weight")

    context = {'public_tweets': public_tweets,
               'video_number': video_number,
               'main_page': main_page,
               'about_page': about_page,
               # 'press_page': press_page,
               # 'partner_page': partner_page,
               'commission_page': commission_page,
               'event_page': event_page,
               'footer_page': footer_page,
               'contact_page': contact_page,
               'research_advisers_page': research_advisers_page,
               'contact_form': contact_form,
               'chair_members': chair_members,
               'other_members': other_members,
               'supporting_members': supporting_members,
               'research_advisers': research_advisers,
               'faq_list': faq_list,
               'faq_page': faq_page,
               'GA_SITE_ID': settings.GA_SITE_ID,
               'GA_SITE_URL': settings.GA_SITE_URL,
               'VIDEO_BASE_URL': settings.VIDEO_BASE_URL,
               'press_releases': press_releases,
               'partners': partners,
               'supporters': supporters,
               'media_contacts': media_contacts,
               'current_events': current_events,
               'past_events': past_events,
               'publications': publications,
               'videos': videos,
               'features': features,
               }

    return render(request, template, context)


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

    else:
        form = ContactForm()



    context = {'contact_form': form,
               'media_contacts': MediaContact.objects.filter(display_on_contact=True).order_by("weight"),
               }

    if request.is_ajax():
        return render(request, 'structure/_contact.html', context)
    else:
        return redirect('contact_redirect_no_ajax')


class CustomRedirectView(RedirectView):
    permanent = False
    query_string = False

    def get_redirect_url(self, *args, **kwargs):

        url_alias = get_object_or_404(UrlAlias, source=kwargs['source'])
        self.url = url_alias.destination

        return super(CustomRedirectView, self).get_redirect_url(*args, **kwargs)
