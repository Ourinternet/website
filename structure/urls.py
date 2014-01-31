from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^$', 'structure.views.home', name='home'),
                       url(r'^contact/$', 'structure.views.contact_submit', name='contact'),
                       )
