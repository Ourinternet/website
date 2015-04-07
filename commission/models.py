from django.db import models, IntegrityError
from django.utils.text import slugify
import re

MEMBER_TYPES = (('chair', 'chair'),
                ('general', 'general'),
                ('supporting', 'supporting'),
                ('research_adviser', 'research adviser')
                )


class Person(models.Model):
    name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    position = models.CharField(max_length=512, blank=True, null=True)
    twitter_handle = models.CharField(max_length=60, blank=True, null=True)
    short_bio = models.TextField(blank=True, null=True)
    partner = models.ForeignKey("Partner", blank=True, null=True)
    website = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        abstract = True

    def slug(self):
        return slugify(self.name)

    def __unicode__(self):
        return self.name


class UniquelySlugable(models.Model):
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:255]

            while type(self).objects.filter(slug=self.slug).exists():
                match_obj = re.match(r'^(.*)-(\d+)$', self.slug)
                if match_obj:
                    next_int = int(match_obj.group(2)) + 1
                    self.slug = match_obj.group(1) + "-" + str(next_int)
                else:
                    self.slug += '-2'

        super(UniquelySlugable, self).save(*args, **kwargs)


class Member(Person):
    member_type = models.CharField(max_length=20, choices=MEMBER_TYPES, default='general')


class Partner(models.Model):
    name = models.CharField(max_length=256)
    short_name = models.CharField(max_length=30, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    website_display = models.CharField(max_length=256, null=True, blank=True)

    description = models.TextField(null=True, blank=True)
    press_description = models.TextField(null=True, blank=True)

    logo = models.ImageField(upload_to='partner_logos', null=True, blank=True)
    weight = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name


class Supporter(models.Model):
    name = models.CharField(max_length=255)
    website = models.URLField(null=True, blank=True)
    weight = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name


class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()
    weight = models.IntegerField(default=0)

    def __unicode__(self):
        return self.question


class MediaContact(models.Model):
    name = models.CharField(max_length=256)
    position = models.CharField(max_length=256)
    company = models.CharField(max_length=256)
    telephone = models.CharField(max_length=40)
    email = models.CharField(max_length=256)

    display_on_contact = models.BooleanField(default=True)
    weight = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name


class PressReleaseFooter(models.Model):
    name = models.CharField(max_length=256)
    media_contacts = models.ManyToManyField('MediaContact', null=True, blank=True)
    partners = models.ManyToManyField('Partner', null=True, blank=True)

    def __unicode__(self):
        return self.name


class PressRelease(UniquelySlugable):
    release_date = models.DateTimeField()
    location = models.TextField()
    title = models.TextField()
    content = models.TextField()
    footer = models.ForeignKey('PressReleaseFooter', null=True, blank=True)
    release_tag = models.TextField(default="For immediate release")
    end_tag = models.CharField(max_length=20, default="-30-")

    def __unicode__(self):
        return self.title


class Event(UniquelySlugable):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.TextField()
    title = models.TextField()
    content = models.TextField()

    def __unicode__(self):
        return self.title


class PublicationType(models.Model):
    name = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name


class Publication(UniquelySlugable):
    title = models.TextField()
    description = models.TextField()
    body = models.TextField(blank=True, null=True)
    publish_date = models.DateField()
    type = models.ForeignKey("PublicationType")
    authors = models.ManyToManyField("Author", through='PublicationAuthor',
                                     blank=True, null=True)
    document = models.FileField(upload_to="publications",
                                blank=True, null=True)
    document_link = models.URLField(null=True, blank=True)
    document_link_title = models.CharField(max_length=128, default="Download PDF")
    image = models.ImageField(upload_to="publications/images",
                              blank=True, null=True)

    def __unicode__(self):
        return self.title

    def get_authors(self):
        return self.authors.order_by('ordered_authors')


class Author(Person):
    pass


class PublicationAuthor(models.Model):
    publication = models.ForeignKey("Publication")
    author = models.ForeignKey("Author", related_name="ordered_authors")
    weight = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return "%s - %s - %d" % (self.publication, self.author, self.weight)

    class Meta:
        ordering = ('weight', )


class Video(UniquelySlugable):
    video_id = models.CharField(max_length=1024)
    title = models.CharField(max_length=1024)
    description = models.TextField()
    weight = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return "%s" % self.title


class Feature(models.Model):
    type_line = models.CharField(max_length=1024, blank=True, null=True)
    title = models.CharField(max_length=1024, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    link = models.CharField(max_length=1024,null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    date_title = models.CharField(max_length=128, default="Release Date")
    disable = models.BooleanField(default=False)
    weight = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return "%s - %s - %d" % (self.type_line, self.title, self.weight)

    class Meta:
        ordering = ('weight', )
