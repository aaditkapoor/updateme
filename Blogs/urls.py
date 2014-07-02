__author__ = 'aadit'

from django.conf.urls import patterns, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('Blogs.views',
                       url(r'^$', 'home', name='home'),
                       url(r'^add/$', 'process_data', name='process_data'),
                       url(r'^latest/$', 'retrieve', name='retrieve'),
                       url(r'^report_an_error/$', 'get_solved_errors', name='get_solved_errors'),
                       url(r'^report/$', 'report_forward', name='report_forward'),
                       url(r'^report/(?P<error>\w+)/$', 'error_report', name='error_report'),
                       url(r'^show_by_user/(?P<user>\w+)/$', 'show_blogs', name='show_blogs'),
                       url(r'^thank/(?P<user>\w+)/$', 'thank', name='thank'),
                       url(r'^like/$', 'like', name='like'),
                       url(r'^like_post/(?P<key>\d+)/$', 'like_post', name='like_post'),
                       url(r'^show_by_blog/(?P<id>\d+)/$', 'show_by_blog', name='show_by_blog'),
                       url(r'^most_liked/$', 'most_liked', name='most_liked'),
)
