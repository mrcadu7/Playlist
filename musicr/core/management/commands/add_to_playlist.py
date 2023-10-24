# from django.core.management.base import BaseCommand
# from core.models import PlaylistItem, Playlist

# class Command(BaseCommand):
#     help = 'Adiciona um item a uma playlist por ID'

#     def add_arguments(self, parser):
#         parser.add_argument('item_id', type=str)
#         parser.add_argument('playlist_name', type=str, choices=['To listen', 'Listened'])

#     def handle(self, *args, **kwargs):
#         item_id = kwargs['item_id']
#         playlist_name = kwargs['playlist_name']

#         # Verifique se o item com o ID fornecido já existe
#         try:
#             item = PlaylistItem.objects.get(item_id=item_id)
#         except PlaylistItem.DoesNotExist:
#             # Se o item não existir, crie-o com o campo 'playlist' definido
#             playlist_name = playlist_name.replace('_', ' ')  # Remover underscore
#             if playlist_name == 'To listen':
#                 playlist = Playlist.objects.get(name='To listen')
#             else:
#                 playlist = Playlist.objects.get(name='Listened')
#             item = PlaylistItem(item_id=item_id, playlist=playlist, status=playlist_name)
#             item.save()

#         # Adicione o item à playlist apropriada
#         playlist.playlistitem_set.add(item)
#         self.stdout.write(self.style.SUCCESS(f'Item adicionado à playlist {playlist_name}: {item_id}'))
