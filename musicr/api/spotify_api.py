import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from datetime import datetime


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

        albums = spotify.artist_albums(artist['id'], album_type='album')

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
                }
                album_info["tracks"].append(track_info)

            artist_info["albums"].append(album_info)

        return artist_info
    else:
        return None
