
from django.conf.urls import patterns,url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('Contact.views',
                       url(r'^$', 'home', name = 'home'),
                       url(r'^contact_request/$','contact_request', name = 'contact_request'),
                       url(r'^notify_by_email(?P<phone_number>\w+)/$','notify_by_email',name = 'notify_by_email'),
                       url(r'^thank/$','thank_you',name = 'thank_you')

)
