from django.shortcuts import render, redirect
from random import randint
from django.conf import settings
from forms import ContactForm
from django.core.mail import EmailMessage
from django.contrib import messages
from django.contrib.flatpages.models import FlatPage
from tweet_cache.models import Tweet
from commission.models import Member, FAQ


def home(request, template="structure/home.html"):

    public_tweets = Tweet.objects.filter(account=settings.TWITTER_USER, hide=False).order_by("-id")[:20]

    video_number = randint(1, 3)

    main_page, created = FlatPage.objects.get_or_create(url='/main/')
    about_page, created = FlatPage.objects.get_or_create(url='/about/')
    press_page, created = FlatPage.objects.get_or_create(url='/press/')
    partner_page, created = FlatPage.objects.get_or_create(url='/partner/')
    commission_page, created = FlatPage.objects.get_or_create(url='/commission/')
    event_page, created = FlatPage.objects.get_or_create(url='/event/')
    footer_page, created = FlatPage.objects.get_or_create(url='/footer/')
    contact_page, created = FlatPage.objects.get_or_create(url='/contact/')
    contact_form = ContactForm()

    faq_page, created = FlatPage.objects.get_or_create(url='/faq/')
    faq_list = FAQ.objects.all().order_by('weight')

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
               'contact_page': contact_page,
               'contact_form': contact_form,
               'chair_members': chair_members,
               'other_members': other_members,
               'faq_list': faq_list,
               'faq_page': faq_page,
               'GA_SITE_ID': settings.GA_SITE_ID,
               'GA_SITE_URL': settings.GA_SITE_URL,
               'public_key': settings.RECAPTCHA_PUBLIC_KEY,
               'VIDEO_BASE_URL': settings.VIDEO_BASE_URL,
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
               'public_key': settings.RECAPTCHA_PUBLIC_KEY,
               }
    return render(request, 'structure/_contact.html', context)

