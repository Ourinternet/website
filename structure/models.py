from django.db import models


class UrlAlias(models.Model):
    source = models.CharField(max_length=1024)
    destination = models.CharField(max_length=1024)

    def __unicode__(self):
        return "%s -> %s" % (self.source, self.destination)

    class Meta:
        verbose_name_plural = 'url aliases'
