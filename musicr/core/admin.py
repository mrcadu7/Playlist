from django.contrib import admin
from core.models.playlist import Playlists, Addition
from core.models.music import Song, Album, Artist



# PLAYLISTS
@admin.register(Playlists)
class PlaylistsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')


@admin.register(Addition)
class AdditionAdmin(admin.ModelAdmin):
    list_display = ('song', 'playlist', 'created_at')
    list_filter = ('playlist', 'created_at')
    

# MUSICS
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('name', 'album', 'genre')
    list_filter = ('album', 'genre')
    

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist')
    list_filter = ('artist', )
    

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('name', )
    
