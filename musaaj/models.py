from django.db import models
from datetime import datetime


class MediaModel(models.Model):
    created_at = models.DateTimeField(default=datetime.now)
    title = models.CharField(max_length=256)
    description = models.TextField()

    class Meta:
        abstract = True

class PhotoModel(MediaModel):
    picture = models.ImageField(upload_to='photo')

class VideoModel(MediaModel):
    video = models.FileField(upload_to='video')

class AudioModel(MediaModel):
    audio = models.FileField(upload_to='audio')
