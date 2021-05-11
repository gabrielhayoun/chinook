from django import forms


class SearchForm(forms.Form):
    """
    Simplest possible form, just a text box for a query
    """
    query = forms.CharField(max_length=100, required=False)
