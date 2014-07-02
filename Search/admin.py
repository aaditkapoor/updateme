from django.contrib import admin
from .models import SiteSection

class SiteSectionAdmin(admin.ModelAdmin):
    list_display = ['section1','section2','section3']


admin.site.register(SiteSection,SiteSectionAdmin)