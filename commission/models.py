from django.db import models
from django.utils.text import slugify


MEMBER_TYPES = (('chair', 'chair'), ('general', 'general'), ('supporting', 'supporting'))


class Member(models.Model):
    name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    position = models.CharField(max_length=512, blank=True, null=True)
    twitter_handle = models.CharField(max_length=60, blank=True, null=True)
    short_bio = models.TextField(blank=True, null=True)
    partner = models.ForeignKey("Partner", blank=True, null=True)
    member_type = models.CharField(max_length=20, choices=MEMBER_TYPES, default='general')

    def slug(self):
        return slugify(self.name)

    def __unicode__(self):
        return self.name


class Partner(models.Model):
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name


class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()
    weight = models.IntegerField()

    def __unicode__(self):
        return self.question

