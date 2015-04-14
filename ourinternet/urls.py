from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from structure.views import CustomRedirectView
admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('structure.urls')),
    url(r'', include('commission.urls')),

    (r'^robots\.txt$', include('robots.urls')),

    (r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^(?P<source>[-\w]+)/$', CustomRedirectView.as_view(), name='redirect')

)


if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))