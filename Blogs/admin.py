from django.contrib import admin

from .models import Blogs, Error


class BlogsAdmin(admin.ModelAdmin):
    list_display = ['author', 'date', 'blog', 'approved', 'unique_key', 'likes']
    search_fields = ['author']
    list_filter = ['author', 'approved', 'date']


class ErrorAdmin(admin.ModelAdmin):
    list_display = ['error', 'date', 'resolved']
    search_fields = ['error']
    list_filter = ['date', 'resolved']


admin.site.register(Blogs, BlogsAdmin)
admin.site.register(Error, ErrorAdmin)
