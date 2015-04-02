from django.shortcuts import render
from django.views.generic import TemplateView
from models import PressRelease, Publication
from random import randint
from django.conf import settings


def press_release(request, slug, template="commission/press_release.html"):

    release = PressRelease.objects.get(slug=slug)

    context = {'release': release,
               }

    return render(request, template, context)


class PublicationPageView(TemplateView):
    template_name = "commission/publication_page.html"

    def get_context_data(self, **kwargs):
        context = super(PublicationPageView, self).get_context_data(**kwargs)

        video_number = randint(1, 3)
        context['video_number'] = video_number
        context['GA_SITE_ID'] = settings.GA_SITE_ID
        context['GA_SITE_URL'] = settings.GA_SITE_URL
        context['publication'] = Publication.objects.get(slug=kwargs['slug'])
        return context