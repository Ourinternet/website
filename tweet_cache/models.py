from django.db import models


class Tweet(models.Model):
    tweet_id = models.BigIntegerField()
    account = models.CharField(max_length=30)
    profile_image_url = models.CharField(max_length=256)
    text = models.CharField(max_length=140)
    processed_text = models.CharField(max_length=1028, blank=True, null=True)
    hide = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s - %s" % (self.account, self.tweet_id)
