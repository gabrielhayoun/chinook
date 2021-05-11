from django.db import models


# TODO: define verbose_name, Meta with order, and __str__ functions

class Track(models.Model):
    """
    A single track in an album
    """
    name = models.CharField(max_length=200)
    composer = models.CharField(max_length=200)
    milliseconds = models.IntegerField()
    bytes = models.IntegerField()
    unitPrice = models.FloatField()
    album = models.ForeignKey('Album', on_delete=models.CASCADE)


class Album(models.Model):
    """
    An album, by a single artist, with several tracks
    """
    title = models.CharField(max_length=200)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)


class Artist(models.Model):
    """
    An artist, that may have many albums
    """
    name = models.CharField(max_length=200)
