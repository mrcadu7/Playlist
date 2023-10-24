import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def ms_to_min_sec(ms):
    total_seconds = ms / 1000
    minutes = int(total_seconds // 60)
    seconds = int(total_seconds % 60)
    return f"{minutes}:{seconds:02d}"


# pega da env o CLIENT_ID e CLIENT_SECRET
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

# Nome do artista que você deseja pesquisar
artist_name =   input(str('Digite o nome do artista desejado: ')).lower()

# Fazer a pesquisa pelo artista
results = spotify.search(q='artist:' + artist_name, type='artist')

# Verificar se há resultados
if results['artists']['items']:
    # Recuperar o PRIMEIRO artista encontrado na pesquisa (geralmente o mais relevante)
    artist = results['artists']['items'][0]

    
    # Imprimir informações sobre o artista
    print("Nome do Artista:", artist['name'])
    print("ID do Artista:", artist['id'])
    print("Imagem do Artista:", artist['images'][0]['url'])
    
    # Obter os álbuns do artista
    albums = spotify.artist_albums(artist['id'], album_type='album')

    # Imprimir os nomes dos álbuns do artista
    for album in albums['items']:
        print("\nÁlbum:", album['name'])
        if album['images']:
            print("Imagem do Álbum:", album['images'][0]['url'],"\n")
        else:
            print("Sem imagem disponível para este álbum")
        
        # Adicione a data de lançamento do álbum
        print("Data de Lançamento:", album['release_date'])
        
        # Obter as faixas do álbum
        tracks = spotify.album_tracks(album['id'])
        
        # Loop pelas faixas do álbum
        for index, track in enumerate(tracks['items'], start=1):
            duration = ms_to_min_sec(track['duration_ms'])
            print(f"{index:2d}. {track['name']} - Duração: {duration}")

else:
    print(f"Artista '{artist_name}' não encontrado no Spotify.")