from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['phone_number','message','date','email','notified','email_sent']
    search_fields = ['phone_number']
    list_filter = ['date','email_sent']


admin.site.register(Contact,ContactAdmin)