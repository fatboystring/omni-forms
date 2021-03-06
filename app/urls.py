# -*- coding: utf-8 -*-
"""
URLS for the omniforms app - Used in testing
"""
from __future__ import unicode_literals

from django.conf.urls import include, url
from django.contrib import admin

from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtailcore import urls as wagtail_urls


urlpatterns = [
    url(r'^django-admin/', include(admin.site.urls)),
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'', include(wagtail_urls))
]
