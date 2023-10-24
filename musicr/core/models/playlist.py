from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from .music import Song

# Create your models here.
class Playlists(models.Model):
    title = models.CharField(max_length=64, default='')
    description = models.CharField(max_length=512)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "playlist"
        verbose_name_plural = "playlists"

    def __str__(self):
        return self.title
        
        
class Addition(models.Model):
    song = models.ForeignKey(Song, related_name="playlists", on_delete=models.CASCADE)
    playlist = models.ForeignKey(Playlists, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "adição"
        verbose_name_plural = "adições"


class Listener(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="favorite_playlists", on_delete=models.CASCADE)
    playlist = models.ForeignKey(Playlists, related_name="listeners", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "ouvinte"
        verbose_name_plural = "ouvintes"
        
    def __str__(self):
        return str(self.user)