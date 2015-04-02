from django.conf.urls import patterns, include, url
from .views import PublicationPageView

urlpatterns = patterns('',
                       url(r'^release/(?P<slug>[-\w]+)/$', 'commission.views.press_release', name='press_release'),
                       url(r'^publication/(?P<slug>[-\w]+)/$', PublicationPageView.as_view(), name='publication'),
                       )
