from django.db import models
from django.utils.text import slugify


class Member(models.Model):
    name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    position = models.CharField(max_length=512, blank=True, null=True)
    twitter_handle = models.CharField(max_length=60, blank=True, null=True)
    short_bio = models.TextField(blank=True, null=True)
    partner = models.ForeignKey("Partner", blank=True, null=True)
    chair = models.BooleanField(default=False)

    def slug(self):
        return slugify(self.name)

    def __unicode__(self):
        return self.name


class Partner(models.Model):
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name