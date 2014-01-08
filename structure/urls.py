from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^$', 'structure.views.home', name='home'),
                       )
