from django import forms
from PetstagramWebsite.photos.models import Photo


class PhotoCreateForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['date_of_publication', 'user']
        widgets = {
            'tagged_pets': forms.SelectMultiple()
        }


class PhotoEditForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['image', 'user', 'date_of_publication']
        widgets = {
            'tagged_pets': forms.SelectMultiple()
        }

