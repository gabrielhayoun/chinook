import datetime

from django.db import models


# TODO: define verbose_name, Meta with order

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

    # FIXME: can it be done just once after the ORM has created the object?
    def ms_to_duration(self):
        minutes = self.milliseconds / 60000
        seconds = (self.milliseconds % 60000) / 1000
        #millis = self.milliseconds % 1000
        return f'%d:%02d' % (minutes, seconds)

    def __str__(self):
        return f'{self.name}, on {self.album}'


class Album(models.Model):
    """
    An album, by a single artist, with several tracks
    """
    title = models.CharField(max_length=200)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}, by {self.artist}'


class Artist(models.Model):
    """
    An artist, that may have many albums
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
