from django.contrib import admin
from models import (Member, Partner, FAQ, PressRelease, MediaContact,
    PressReleaseFooter, Supporter, Event, Publication, Author,
    PublicationType, PublicationAuthor, Video, Feature, FeatureLink,
    OrderedFeatureLink, Webcast)


class PublicationAuthorInline(admin.TabularInline):
    model = PublicationAuthor
    extra = 1


class PublicationAdmin(admin.ModelAdmin):
    inlines = (PublicationAuthorInline, )


class FeatureLinkInline(admin.TabularInline):
    model = OrderedFeatureLink
    extra = 1


class FeatureAdmin(admin.ModelAdmin):
    inlines = (FeatureLinkInline, )


admin.site.register(Member)
admin.site.register(Partner)
admin.site.register(FAQ)
admin.site.register(PressRelease)
admin.site.register(MediaContact)
admin.site.register(PressReleaseFooter)
admin.site.register(Supporter)
admin.site.register(Event)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(PublicationType)
admin.site.register(Author)
admin.site.register(PublicationAuthor)
admin.site.register(Video)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(FeatureLink)
admin.site.register(Webcast)

