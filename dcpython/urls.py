from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    url(r'^events/', include("events.urls")),
    # FIXME: refactor all donation views into support/urls.py, consider renaming app
    url(r'^donate/$', 'support.views.support', name='support'),
    url(r'^donor/(?P<secret>[\w\-_]+=?=?=?)/$', 'support.views.donor_update', name='donor_update'),
    url(r'^make_donation$', 'support.views.make_donation', name='make_donation'),
    url(r'^about/$', 'app.views.about', name='about'),
    url(r'^deals/$', 'app.views.deals', name='deals'),
    url(r'^resources/$', 'app.views.resources', name='resources'),
    url(r'^legal/$', 'app.views.legal', name='legal'),
    url(r'^contact/$', 'app.views.contact', name='contact'),
    # url(r'^$', 'dcpython.views.home', name='home'),
    # url(r'^dcpython/', include('dcpython.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
