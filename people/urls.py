# -*- coding: utf-8 -*-
from django.conf.urls import include, patterns, url
from .views import DetailView, ListView


urls = patterns('people.views',

    url(r'^(?P<slug>[\w-]+)$',
        DetailView.as_view(), name='people_detail'),

    url(r'^$',
        ListView.as_view(), name='people_list'),
)

urlpatterns = patterns(
    '', (r'^', include(urls, namespace='people')),
)
