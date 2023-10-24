# Generated by Django 4.2.6 on 2023-10-20 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlistitem',
            name='item_type',
        ),
        migrations.AddField(
            model_name='playlist',
            name='items',
            field=models.ManyToManyField(related_name='playlists', to='core.playlistitem'),
        ),
    ]
