# -*- coding: utf-8 -*-
from django.conf.urls import include, patterns, url
from .views import ListView
#from .views import DetailView, ListView


urls = patterns('networks.views',

    # url(r'^(?P<slug>[\w-]+)$',
    #     DetailView.as_view(), name='networks_detail'),

    url(r'^$',
        ListView.as_view(), name='networks_list'),
)

urlpatterns = patterns(
    '', (r'^', include(urls, namespace='networks')),
)
