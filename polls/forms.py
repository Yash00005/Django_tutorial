from django import forms
from .models import siterating

class ratingform(forms.ModelForm):
    class Meta:
        model = siterating
        fields = ['rating', 'comment' ]