from django.contrib import admin
from django.conf import settings

from core.models import Book, Author, Tag


class BookAdmin(admin.ModelAdmin):

    def cover_image(self, instance):
        if not instance.cover:
            return ''
        return '<img src="%s" width="90" height="120" />' % instance.cover.url
    cover_image.short_description = 'Cover'
    cover_image.allow_tags = True

    def tags_list(self, instance):
        return ', '.join([t.name for t in instance.tags.all()])
    tags_list.short_description = 'Tags'

    def external_link(self, instance):
        if not instance.link:
            return ''
        return '<a href="%s" title="Click to visit Amazon.com" target="_blank">Amazon</a>' % instance.link
    external_link.short_description = 'Link'
    external_link.allow_tags = True

    site_header = 'Coruja'
    site_title = 'Coruja'
    ordering = ['title']
    list_display = ('cover_image', 'title', 'pub_date', 'tags_list', 'external_link')
    search_fields = ['title']
    list_filter = ('tags',)
    list_per_page = 30



admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Tag)
