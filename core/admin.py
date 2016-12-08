from django.contrib import admin
from django.conf import settings

from core.models import Book, Author, Tag


class BookAdmin(admin.ModelAdmin):

    def cover_image(self, instance):
        return '<img src="%s/%s" width="90" height="120" />' % (settings.MEDIA_URL, instance.cover)
    cover_image.short_description = 'Cover'
    cover_image.allow_tags = True

    def tags_list(self, instance):
        return ','.join([t.name for t in instance.tags.all()])
    tags_list.short_description = 'Tags'

    site_header = 'Coruja'
    site_title = 'Coruja'
    ordering = ['title']
    list_display = ('cover_image', 'title', 'pub_date', 'tags_list')
    search_fields = ['title']
    list_filter = ('tags',)
    list_per_page = 31
    save_on_top = True


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Tag)
