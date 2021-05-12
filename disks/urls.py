from django.urls import path
from . import views

urlpatterns = [
    path('', views.album_list, name='album_list'),
    path('<int:album_id>', views.album_tracks, name='album_tracks'),
    path('album_creation', views.album_creation, name='album_creation'),
]
