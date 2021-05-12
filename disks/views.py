from django.db.models import Q
from django.shortcuts import redirect, render, get_list_or_404, get_object_or_404

from .forms import SearchForm, AlbumForm
from .models import Album


def album_list(request):
    """
    Get all albums from database and inject them into the album_list template
    """
    form = SearchForm(request.POST or None)

    if form.is_valid():
        query = form.cleaned_data['query']
        albums = Album.objects.filter(
            Q(title__icontains=query) |
            Q(artist__name__icontains=query)
        )
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


def album_creation(request):
    """
    Display a form to collect data and create new album
    """
    form = AlbumForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('album_list')
    else:
        return render(request, 'disks/album_creation.html', locals())
