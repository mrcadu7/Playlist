from django.shortcuts import render
from api.spotify_api import get_artist_info, get_track_info, get_or_create_album, search_artists
from django import forms
from core.models.playlist import Playlists, Addition
from core.models.music import Song
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse


class ArtistNameForm(forms.Form):
    artist_name = forms.CharField(label='', max_length=100)


class AddToPlaylistForm(forms.Form):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(AddToPlaylistForm, self).__init__(*args, **kwargs)
        self.fields['playlist'].queryset = Playlists.objects.filter(user=user)

    playlist = forms.ModelChoiceField(queryset=Playlists.objects.none())
    spotify_id = forms.CharField(widget=forms.HiddenInput())



def autocomplete(request):
    if 'term' in request.GET:
        artists = search_artists(request.GET.get('term'))
        names = [artist['name'] for artist in artists]
        return JsonResponse(names, safe=False)
    return render(request, 'index.html')


def index(request):
    artist_data = None
    message = None
    playlists = Playlists.objects.all()

    if request.method == 'POST':
        form = ArtistNameForm(request.POST)
        if form.is_valid():
            artist_name = form.cleaned_data['artist_name']
            artist_data = get_artist_info(artist_name)

            if artist_data:
                for album in artist_data['albums']:
                    for track in album['tracks']:
                        if request.user.is_authenticated:
                            track['form'] = AddToPlaylistForm(initial={'spotify_id': track['track_id']}, user=request.user)
            else:
                message = f"Artista '{artist_name}' não encontrado no Spotify."
        
    else:
        form = ArtistNameForm()

    return render(request, 'index.html', {'artist_data': artist_data,
                                          'form': form,
                                          'message': message,
                                          'playlists': playlists})




def add_to_playlist(request):
    # Certifique-se de que o usuário está autenticado antes de tentar modificar a playlist
    if not request.user.is_authenticated:
        return JsonResponse({'success': False, 'message': 'Usuário não está logado'})

    if request.method == 'POST':
        form = AddToPlaylistForm(request.POST, user=request.user)
        if form.is_valid():
            playlist = form.cleaned_data['playlist']
            spotify_id = form.cleaned_data['spotify_id']
            # Obtenha o usuário logado
            user = request.user
            # Verifique se o usuário tem permissão para modificar a playlist
            if playlist.user == user:
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
                # Verifique se a música já está na playlist
                if not Addition.objects.filter(song=song, playlist=playlist).exists():
                    # Crie um novo objeto Addition com a música e a playlist
                    addition = Addition.objects.create(song=song, playlist=playlist)
                    return JsonResponse({'success': True, 'message': 'Música adicionada com sucesso'})
                else:
                    return JsonResponse({'success': False, 'message': 'Música já existe na playlist'})
            else:
                return JsonResponse({'success': False, 'message': 'Usuário não tem permissão para modificar a playlist'})

    return JsonResponse({'message': 'Erro na solicitação AJAX'}, status=400)


# def create_playlist(request):
#     if request.method == 'POST':
#         form = CreatePlaylistForm(request.POST) # necessário criar essa classe
#         if form.is_valid():
#             title = form.cleaned_data['title']
#             description = form.cleaned_data['description']
#             # Adicione o usuário à playlist
#             user = request.user
#             playlist = Playlists.objects.create(user=user, title=title, description=description)
#             return JsonResponse({'success': True, 'message': 'Playlist criada com sucesso'})
#     return JsonResponse({'message': 'Erro na solicitação AJAX'}, status=400)


def view_playlist(request, playlist_id):
    # Obtenha o usuário logado
    user = request.user
    # Filtre a playlist pelo usuário
    playlist = Playlists.objects.filter(user=user, id=playlist_id).first()
    if playlist:
        additions = Addition.objects.filter(playlist=playlist)
        songs = [addition.song for addition in additions]
        playlists = Playlists.objects.all()
        return render(request, 'view_playlist.html', {'songs': songs, 'playlist': playlist, 'playlists': playlists})
    else:
        return HttpResponse('Playlist não encontrada ou não pertence ao usuário', status=404)

def list_playlists(request):
    # Obtenha o usuário logado
    user = request.user
    # Filtre as playlists pelo usuário
    playlists = Playlists.objects.filter(user=user)
    playlist_songs = {}
    for playlist in playlists:
        additions = Addition.objects.filter(playlist=playlist)
        songs = [addition.song for addition in additions]
        playlist_songs[playlist] = songs
    return render(request, 'list_playlists.html', {'playlist_songs': playlist_songs, 'user': user})

