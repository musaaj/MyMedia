from django import forms
from .models import PhotoModel

class PhotoForm(forms.ModelForm):
    class Meta:
        model = PhotoModel
        fields = ('title', 'description', 'picture')
        widgets = {
            'description': forms.Textarea(
                attrs={
                    'class': 'w3-input w3-round w3-border w3-padding',
                    'placeholder': 'Picture description',
                    'rows': 2
                }
            ),
            'title': forms.TextInput(
                attrs={
                    'class': 'w3-input w3-round w3-border w3-padding',
                    'placeholder': 'Title'
                }
            ),
            'picture': forms.FileInput(
                attrs={
                    'class': 'w3-bar'
                }
            )
        }
        labels = {
            'title': False,
            'description': False,
            'Picture': False
        }
        error_messages = {
            'picture': {
                '': 'w3-red'
            }
        }

    def clean_picture(self):
        picture = self.cleaned_data.get('picture')
        if picture:
            if picture.size > 2 * 1024 * 1024:
                raise forms.ValidationError(
                        'The image file is too large (maximum size is 2MB)'
                    )
            if not picture.content_type.startswith('image/'):
                raise forms.ValidationError(
                        """The uploaded file is not an image 
                        (allowed formats are JPEG, PNG, and GIF)"""
                    )
        return picture

