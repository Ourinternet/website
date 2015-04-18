from django.shortcuts import render
from django.views.generic import TemplateView
from .models import PressRelease, Publication, Webcast
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
            alias = UrlAlias.objects.get(source='publication/{}'.format(kwargs['slug']))
            publication = Publication.objects.get(slug=alias.destination[:13])

        footer_page, created = FlatPage.objects.get_or_create(url='/footer/')
        video_number = randint(1, 3)
        context['video_number'] = video_number
        context['GA_SITE_ID'] = settings.GA_SITE_ID
        context['GA_SITE_URL'] = settings.GA_SITE_URL
        context['publication'] = publication
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