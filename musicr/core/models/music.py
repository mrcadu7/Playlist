from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=64, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "artista"
        verbose_name_plural = "artistas"
    
    def __str__(self):
        return self.name
    

class Album(models.Model):
    title = models.CharField(max_length=64)
    artist = models.ForeignKey(Artist, related_name='albums', on_delete=models.CASCADE)
    year = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "album"
        verbose_name_plural = "albums"
    
    def __str__(self):
        return self.title
    

class Song(models.Model):
    spotify_id = models.CharField(max_length=200, unique=True)
    album = models.ForeignKey(Album, related_name='songs', on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    genre = models.CharField(max_length=64)
    duration = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "musica"
        verbose_name_plural = "musicas"
    
    def __str__(self):
        return str(self.name)
    
