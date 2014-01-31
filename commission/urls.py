from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^release/(?P<slug>[-\w]+)/$', 'commission.views.press_release', name='press_release'),
                       )
