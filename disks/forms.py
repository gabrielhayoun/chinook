from django import forms
from .models import Album, Artist

class SearchForm(forms.Form):
    """
    Simplest possible form, just a text box for a query
    """
    query = forms.CharField(max_length=100, required=False, label='Search in album titles')


class AlbumForm(forms.ModelForm):
    """
    A django-generated form based on the Album model
    """
    class Meta:
        model = Album
        fields = '__all__'

    def clean(self):
        """
        Validates a new album only if it's not a duplicate
        """
        cleaned_data = super(AlbumForm, self).clean()
        title = cleaned_data['title']
        artist = cleaned_data['artist']

        duplicate = Album.objects.filter(title=title).filter(artist=artist)
        if duplicate.exists():
            raise forms.ValidationError('Album with same title and artist already in database')
        return cleaned_data
