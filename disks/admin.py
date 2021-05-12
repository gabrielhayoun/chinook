from django.contrib import admin
from .models import Track, Album, Artist


class AlbumAdmin(admin.ModelAdmin):
    """
    Album administration customization

    Search both album title and name of the associated artist
    """
    list_display = ('title', 'artist')
    search_fields = ('title', 'artist__name') ## __ allows to search in the artist table
    list_filter = ('artist', )


class TrackAdmin(admin.ModelAdmin):
    """
    Track administration customization

    Provides the track_artist() method to add a column with the track's artist
    Search track name, but also title of the associated album, and name of
    the associated album's artist
    """
    list_display = ('name', 'album', 'track_artist')
    search_fields = ('name', 'album__title', 'album__artist__name')
    list_filter = ('album', )

    def track_artist(self, track):
        return track.album.artist

    track_artist.short_description = 'Artist'


# Register models into the administration application
admin.site.register(Track, TrackAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Artist)
