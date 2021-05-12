from django import forms
from .models import Album

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
