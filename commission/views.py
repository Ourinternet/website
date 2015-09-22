from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import PressRelease, Publication, Webcast, Video, Event
from random import randint
from django.conf import settings
from django.contrib.flatpages.models import FlatPage
from structure.models import UrlAlias


def press_release(request, slug, template="commission/press_release.html"):

    release = PressRelease.objects.get(slug=slug)

    context = {'release': release,
               }

    return render(request, template, context)


class PublicationPageView(TemplateView):
    template_name = "commission/publication_page.html"

    def get_context_data(self, **kwargs):
        context = super(PublicationPageView, self).get_context_data(**kwargs)

        try:
            publication = Publication.objects.get(slug=kwargs['slug'])
        except Publication.DoesNotExist:
            alias = get_object_or_404(UrlAlias, source='publication/{}'.format(kwargs['slug']))
            publication = Publication.objects.get(slug=alias.destination[13:])

        footer_page, created = FlatPage.objects.get_or_create(url='/footer/')
        video_number = randint(1, 3)
        context['video_number'] = video_number
        context['GA_SITE_ID'] = settings.GA_SITE_ID
        context['GA_SITE_URL'] = settings.GA_SITE_URL
        context['publication'] = publication
        context['footer_page'] = footer_page
        return context


class VideoPageView(TemplateView):
    template_name = "commission/video_page.html"

    def get_context_data(self, **kwargs):
        context = super(VideoPageView, self).get_context_data(**kwargs)

        try:
            video = Video.objects.get(slug=kwargs['slug'])
        except Video.DoesNotExist:
            alias = get_object_or_404(UrlAlias, source='video/{}'.format(kwargs['slug']))
            video = Video.objects.get(slug=alias.destination[13:])

        footer_page, created = FlatPage.objects.get_or_create(url='/footer/')
        video_number = randint(1, 3)
        context['video_number'] = video_number
        context['GA_SITE_ID'] = settings.GA_SITE_ID
        context['GA_SITE_URL'] = settings.GA_SITE_URL
        context['video'] = video
        context['footer_page'] = footer_page
        return context


class EventPageView(TemplateView):
    template_name = "commission/event_page.html"

    def get_context_data(self, **kwargs):
        context = super(EventPageView, self).get_context_data(**kwargs)

        try:
            event = Event.objects.get(slug=kwargs['slug'])
        except Event.DoesNotExist:
            alias = get_object_or_404(UrlAlias, source='event/{}'.format(kwargs['slug']))
            event = Event.objects.get(slug=alias.destination[13:])

        footer_page, created = FlatPage.objects.get_or_create(url='/footer/')
        video_number = randint(1, 3)
        context['video_number'] = video_number
        context['GA_SITE_ID'] = settings.GA_SITE_ID
        context['GA_SITE_URL'] = settings.GA_SITE_URL
        context['event'] = event
        context['footer_page'] = footer_page
        return context


class PressReleasePageView(TemplateView):
    template_name = "commission/press_release_page.html"

    def get_context_data(self, **kwargs):
        context = super(PressReleasePageView, self).get_context_data(**kwargs)

        try:
            press_release = PressRelease.objects.get(slug=kwargs['slug'])
        except PressRelease.DoesNotExist:
            alias = get_object_or_404(UrlAlias, source='press/{}'.format(kwargs['slug']))
            press_release = PressRelease.objects.get(slug=alias.destination[13:])

        footer_page, created = FlatPage.objects.get_or_create(url='/footer/')
        video_number = randint(1, 3)
        context['video_number'] = video_number
        context['GA_SITE_ID'] = settings.GA_SITE_ID
        context['GA_SITE_URL'] = settings.GA_SITE_URL
        context['press_release'] = press_release
        context['footer_page'] = footer_page
        return context


class WebCastPageView(TemplateView):
    template_name = "commission/webcast_page.html"

    def get_context_data(self, **kwargs):
        context = super(WebCastPageView, self).get_context_data(**kwargs)

        webcasts = Webcast.objects.filter(disabled=False)
        footer_page, created = FlatPage.objects.get_or_create(url='/footer/')
        webcasts_instructions_page, created = FlatPage.objects.get_or_create(url='/webcasts/instructions/')
        video_number = randint(1, 3)
        context['webcasts'] = webcasts
        context['video_number'] = video_number
        context['GA_SITE_ID'] = settings.GA_SITE_ID
        context['GA_SITE_URL'] = settings.GA_SITE_URL
        context['footer_page'] = footer_page
        context['webcasts_instructions_page'] = webcasts_instructions_page
        return context
