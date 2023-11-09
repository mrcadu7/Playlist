# MUSICR

Um humilde criador de playlists para estudos


## Como funciona?

No momento ele funciona apenas como um "buscador" com opções de criar playlists.
Usuários deverão se cadastrar e logar para terem acesso a criação de playlists
No futuro é pensado, além na melhoria da estilização, features de Rate para que usuários avaliem suas músicas e a opção de migrar a playlist para ouvir no spotify.


## Como desenvolver?

1. Clone o repositório.
2. Crie uma virtualenv com python 3.11
3. Ative a virtualenv
4. Instale as dependências
5. Para uso mais dinâmico, criar arquivo manage.bat em .venv/Scripts/
6. Setar em .venv/Scripts/manage.bat @python "CAMINHO RELATIVO OU ABSOLUTO DO manage.py" %*
7. Cadastre-se e obtenha acesso a API do spotify
8. Adicione em sua ENV o ID e Secret fornecidos pelo dashboard do Spotify
9. Caso queira utilizar autenticação Google, cadastre-se e obtenha acesso a API do Google para provider

```console
git clone https://github.com/mrcadu7/Playlist.git
cd playlist
python -m venv .venv
.venv/Scripts/Activate.ps1  
pip install -r requirements-dev.txt
$env:SPOTIPY_CLIENT_SECRET="XXXSECRETXXX"
$env:SPOTIPY_CLIENT_ID="XXXIDXXX"
$env:SPOTIPY_REDIRECT_URI="http://localhost/"
manage runserver
```
