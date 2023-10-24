from django.shortcuts import render
from api.spotify_api import get_artist_info
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404




class ArtistNameForm(forms.Form):
    artist_name = forms.CharField(label='', max_length=100)


def index(request):
    artist_data = None
    message = None

    if request.method == 'POST':
        form = ArtistNameForm(request.POST)
        if form.is_valid():
            artist_name = form.cleaned_data['artist_name']
            artist_data = get_artist_info(artist_name)

            if not artist_data:
                message = f"Artista '{artist_name}' não encontrado no Spotify."
        
    else:
        form = ArtistNameForm()

    return render(request, 'index.html', {'artist_data': artist_data, 'form': form, 'message': message})

