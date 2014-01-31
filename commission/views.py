from django.shortcuts import render
from models import PressRelease


def press_release(request, slug, template="commission/press_release.html"):

    release = PressRelease.objects.get(slug=slug)

    context = {'release': release,
               }

    return render(request, template, context)

