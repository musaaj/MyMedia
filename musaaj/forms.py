from django import forms
from .models import PhotoModel, VideoModel, AudioModel

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
                'class': 'w3-red'
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


class VideoForm(forms.ModelForm):
    class Meta:
        model = VideoModel
        fields = ['title', 'description', 'video']
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
            'video': forms.FileInput(
                attrs={
                    'class': 'w3-bar'
                }
            )
        }
        labels = {
            'title': False,
            'description': False,
            'video': False
        }

    def clean_video(self):
        video = self.cleaned_data.get('video')
        if video:
            if video.size > 20 * 1024 * 1024:
                raise forms.ValidationError('File too larg')
            if not video.content_type.startswith('video/'):
                raise forms.ValidationError('Invalid video format')
        return video


class AudioForm(forms.ModelForm):
    class Meta:
        model = AudioModel
        fields = ['title', 'description', 'audio']
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
            'audio': forms.FileInput(
                attrs={
                    'class': 'w3-bar'
                }
            )
        }
        labels = {
            'title': False,
            'description': False,
            'audio': False
        }

    def clean_audio(self):
        audio = self.cleaned_data.get('audio')
        if audio:
            if audio.size > 20 * 1024 * 1024:
                raise forms.ValidationError('File too larg')
            if not audio.content_type.startswith('audio/'):
                raise forms.ValidationError('Invalid audio format')
        return audio
