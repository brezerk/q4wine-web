# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.conf import settings
from q4wine.rss.views import RssSiteNewsFeed, AtomSiteNewsFeed
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from docs.models import Doc

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

info_dict = {
    'queryset': Doc.objects.all(),
}

sitemaps = {
    'flatpages': FlatPageSitemap,
    'docs': GenericSitemap(info_dict, priority=0.6),
}


urlpatterns = patterns('',
    (r'^$', 'news.views.news'),
    (r'^page/(?P<page>\d+)/$', 'news.views.news'),
    (r'^news/(?P<newsid>\d+)/$', 'news.views.viewNews'),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^rss/$', RssSiteNewsFeed()),
    (r'^atom/$', AtomSiteNewsFeed()),
    (r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    (r'^documentation/(?P<language>.*)/index.html$', 'docs.views.index'),
    (r'^documentation/(?P<language>.*)/(?P<slug>.*).html$', 'docs.views.show'),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^(?P<path>robots.txt)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^xmlexport/searchApp/(?P<pattern>.*)/(?P<page>\d+)/$', 'xmlexport.views.searchApp'),
    (r'^xmlexport/searchApp/(?P<pattern>.*)/$', 'xmlexport.views.searchApp'),
    (r'^xmlexport/viewApp/(?P<appid>\d+)/$', 'xmlexport.views.viewApp'),
    (r'^xmlexport/viewTest/(?P<appid>\d+)/(?P<verid>\d+)/(?P<testid>\d+)/$', 'xmlexport.views.viewTest'),
    (r'^xmlexport/viewTest/(?P<appid>\d+)/(?P<verid>\d+)/$', 'xmlexport.views.viewTest'),
    (r'^xmlexport/viewCategory/(?P<catid>\d+)/$', 'xmlexport.views.viewCategory'),
    (r'^xmlexport/.*', 'xmlexport.views.index'),
)
