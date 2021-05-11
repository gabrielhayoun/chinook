from django.shortcuts import render, get_list_or_404, get_object_or_404

from .forms import SearchForm
from .models import Album


def album_list(request):
    """
    Get all albums from database and inject them into the album_list template
    """
    form = SearchForm(request.POST or None)

    if form.is_valid():
        query = form.cleaned_data['query']
        albums = Album.objects.filter(title__icontains=query) #, artist__name__icontains=query)
    else:
        albums = get_list_or_404(Album)
    return render(request, 'disks/album_list.html', locals())


def album_tracks(request, album_id):
    """
    Get all tracks from the specified album
    :param request: The incoming request
    :param album_id: The album's ID
    """
    album = get_object_or_404(Album, pk=album_id)
    tracks = album.track_set.all()
    return render(request, 'disks/album_tracks.html', locals())
