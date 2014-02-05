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
    short_name = models.CharField(max_length=30, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    website_display = models.CharField(max_length=256, null=True, blank=True)

    description = models.TextField(null=True, blank=True)
    press_description = models.TextField(null=True, blank=True)

    logo = models.ImageField(upload_to='partner_logos', null=True, blank=True)
    weight = models.IntegerField()

    def __unicode__(self):
        return self.name


class Supporter(models.Model):
    name = models.CharField(max_length=255)
    website = models.URLField(null=True, blank=True)
    weight = models.IntegerField()

    def __unicode__(self):
        return self.name


class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()
    weight = models.IntegerField()

    def __unicode__(self):
        return self.question


class MediaContact(models.Model):
    name = models.CharField(max_length=256)
    position = models.CharField(max_length=256)
    company = models.CharField(max_length=256)
    telephone = models.CharField(max_length=40)
    email = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name


class PressReleaseFooter(models.Model):
    name = models.CharField(max_length=256)
    media_contacts = models.ManyToManyField('MediaContact', null=True, blank=True)
    partners = models.ManyToManyField('Partner', null=True, blank=True)

    def __unicode__(self):
        return self.name


class PressRelease(models.Model):
    release_date = models.DateTimeField()
    location = models.TextField()
    title = models.TextField()
    content = models.TextField()
    footer = models.ForeignKey('PressReleaseFooter', null=True, blank=True)
    release_tag = models.TextField(default="For immediate release")
    end_tag = models.CharField(max_length=20, default="-30-")
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:255]
        super(PressRelease, self).save(*args, **kwargs)

