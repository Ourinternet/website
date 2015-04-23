from django.conf.urls import patterns, include, url
from .views import PublicationPageView, WebCastPageView, EventPageView, \
    VideoPageView, PressReleasePageView

urlpatterns = patterns('',
                       url(r'^release/(?P<slug>[-\w]+)/$', 'commission.views.press_release', name='press_release'),
                       url(r'^publication/(?P<slug>[-\w]+)/$', PublicationPageView.as_view(), name='publication'),
                       url(r'^event/(?P<slug>[-\w]+)/$', EventPageView.as_view(), name='event'),
                       url(r'^video/(?P<slug>[-\w]+)/$', VideoPageView.as_view(), name='video'),
                       url(r'^press/(?P<slug>[-\w]+)/$', PressReleasePageView.as_view(), name='press'),
                       url(r'^live/$', WebCastPageView.as_view(), name='webcast'),
                       )
