from django.shortcuts import render
from api.spotify_api import get_artist_info, get_track_info, get_or_create_album
from django import forms
from core.models.playlist import Playlists, Addition
from core.models.music import Song
from django.shortcuts import render, redirect


class ArtistNameForm(forms.Form):
    artist_name = forms.CharField(label='', max_length=100)


class AddToPlaylistForm(forms.Form):
    playlist = forms.ModelChoiceField(queryset=Playlists.objects.all())
    spotify_id = forms.CharField(widget=forms.HiddenInput())


def index(request):
    artist_data = None
    message = None

    if request.method == 'POST':
        form = ArtistNameForm(request.POST)
        if form.is_valid():
            artist_name = form.cleaned_data['artist_name']
            artist_data = get_artist_info(artist_name)

            if artist_data:
                for album in artist_data['albums']:
                    for track in album['tracks']:
                        track['form'] = AddToPlaylistForm(initial={'spotify_id': track['track_id']})
            else:
                message = f"Artista '{artist_name}' não encontrado no Spotify."
        
    else:
        form = ArtistNameForm()

    return render(request, 'index.html', {'artist_data': artist_data, 'form': form, 'message': message})


def add_to_playlist(request):
    if request.method == 'POST':
        form = AddToPlaylistForm(request.POST)
        if form.is_valid():
            playlist = form.cleaned_data['playlist']
            spotify_id = form.cleaned_data['spotify_id']

            # Obtenha as informações da faixa
            track_info = get_track_info(spotify_id)
            
            song, created = Song.objects.get_or_create(
            spotify_id=spotify_id,
            defaults={
                'name': track_info['name'],
                'duration': track_info['duration'],
                'album': get_or_create_album(track_info['album_name'], track_info['artist_name']),
            }
        )
            # Crie um novo objeto Addition com a música e a playlist
            addition = Addition.objects.create(song=song, playlist=playlist)

    return redirect('index')