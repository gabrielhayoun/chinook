from django.shortcuts import render, get_list_or_404, get_object_or_404

from .models import Album


def album_list(request):
    """
    Get all albums from database and inject them into the album_list template
    """
    albums = get_list_or_404(Album)
    return render(request, 'disks/album_list.html', locals())


def album_tracks(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    tracks = album.track_set.all()
    return render(request, 'disks/album_tracks.html', locals())
