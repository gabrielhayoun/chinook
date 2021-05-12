from django.contrib import admin
from .models import Track, Album, Artist


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist')
    list_filter = ('artist', )
    search_fields = ('title', )


# Register your models here.
admin.site.register(Track)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Artist)
