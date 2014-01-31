from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('structure.urls')),
    url(r'', include('commission.urls')),

    (r'^robots\.txt$', include('robots.urls')),

    (r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
