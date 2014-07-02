from django.contrib import admin
from .models import Helping


class HelpingAdmin(admin.ModelAdmin):
    list_display = ['query','date','name','working','completed']
    search_fields = ['name','date']
    list_filter = ['date','completed']




admin.site.register(Helping,HelpingAdmin)
