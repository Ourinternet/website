from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^$', 'structure.views.home', name='home'),
                       url(r'^#contact$', 'structure.views.home', name='contact_redirect_no_ajax'),
                       url(r'^contact/$', 'structure.views.contact_submit', name='contact'),
                       )
