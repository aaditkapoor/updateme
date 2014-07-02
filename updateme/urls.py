from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$','updateme.views.home',name = 'home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^error/(?P<error_q>\w+)/','updateme.views.process_error',name = 'process_error'),
)

urlpatterns += patterns('',
                 url(r'^blog/',include('Blogs.urls')),
                 url(r'^help/',include('Helper.urls')),
                 url(r'^contact/',include('Contact.urls')),
                 url(r'^search_author/$','Search.views.search_author',name = 'search_author'),
                 url(r'^search_section/$','Search.views.search_section', name = 'search_section'),
                 url(r'^search_blog/$','Search.views.search_blog',name = 'search_blog'),


)

