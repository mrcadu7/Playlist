import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from datetime import datetime
from core.models.music import Album, Artist
from django.http import JsonResponse


def parse_release_date(date_str):
    try:
        # verifica se ta no padrão "YYYY-MM-DD"
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        try:
            # se der merda, verifica se ta no padrão "YYYY"
            return datetime.strptime(date_str, "%Y").date()
        except ValueError:
            # Se ainda falhar, vai tomar no cu
            return None


def search_artists(request):
    artist_name = request.GET.get('q', '')
    limit = 10
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    results = spotify.search(q='artist:' + artist_name, type='artist', limit=limit)
    artists = []
    if results['artists']['items']:
        for artist in results['artists']['items']:
            artist_info = {
                "name": artist['name'],
            }
            artists.append(artist_info)
    return JsonResponse(artists, safe=False)


def get_artist_info(artist_name):
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

    # Fazer a pesquisa pelo artista
    results = spotify.search(q='artist:' + artist_name, type='artist')

    if results['artists']['items']:
        artist = results['artists']['items'][0]
        artist_info = {
            "name": artist['name'],
            "id": artist['id'],
            "image_url": artist['images'][0]['url'],
            "albums": [],
        }
        
        albums = spotify.artist_albums(artist['id'], album_type='album', limit=50)

        for album in albums['items']:
            album_info = {
                "name": album['name'],
                "album_id": album['id'],
                "release_date": parse_release_date(album['release_date']),
                "image_url": album['images'][0]['url'] if album['images'] else None,
                "tracks": [],
            }
            tracks = spotify.album_tracks(album['id'])

            for track in tracks['items']:
                duration = track['duration_ms']
                track_info = {
                    "name": track['name'],
                    "track_id": track['id'],
                    "duration": duration,
                    "album_name": album['name'],  # Adicione o nome do álbum
                    "artist_name": artist['name'],  # Adicione o nome do artista
                }
                album_info["tracks"].append(track_info)

            artist_info["albums"].append(album_info)

        return artist_info
    else:
        return None


def get_track_info(track_id):
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    track = spotify.track(track_id)

    track_info = {
        'name': track['name'],
        'duration': track['duration_ms'],
        'album_name': track['album']['name'],
        'artist_name': ', '.join([artist['name'] for artist in track['artists']])
    }

    return track_info


def get_or_create_album(album_name, artist_name):
    artist, created = Artist.objects.get_or_create(name=artist_name)
    album, created = Album.objects.get_or_create(title=album_name, artist=artist)

    return album


def ms_to_min_sec(ms):
    total_seconds = ms / 1000
    minutes = int(total_seconds // 60)
    seconds = int(total_seconds % 60)
    return f"{minutes}:{seconds:02d}"