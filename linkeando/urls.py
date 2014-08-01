#!/usr/bin/env python
# -*- coding: utf-8 *-*
from django.conf.urls import patterns, url


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'linkeando.views.home', name='home'),
    url(r'^plus/(\d+)$', 'linkeando.views.plus', name='plus'),
    url(r'^minus/(\d+)$', 'linkeando.views.minus', name='minus'),
    url(r'^categoria/(\d+)$', 'linkeando.views.categoria', name='categoria'),
    url(r'^add/$', 'linkeando.views.add', name='add'),
)
