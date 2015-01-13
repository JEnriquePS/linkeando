#!/usr/bin/env python
# -*- coding: utf-8 *-*
from django.conf.urls import patterns, url


urlpatterns = patterns('apps.linkeando.views',
    url(r'^$', 'home', name='home'),
    url(r'^plus/(\d+)$', 'plus', name='plus'),
    url(r'^minus/(\d+)$', 'minus', name='minus'),
    url(r'^categoria/(\d+)$', 'categoria', name='categoria'),
    url(r'^add/$', 'add', name='add'),
)
