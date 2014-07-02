__author__ = 'aadit'

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('Helper.views',

        url(r'^$','home',name = 'home'),
        url(r'^introduction/$','introduction',name = 'introduction'),
        url(r'^submit_feature/$','submit_feature',name = 'submit_feature'),
        url(r'^process_feature/$','process_feature',name = 'process_feature'),

)
