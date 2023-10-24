# Generated by Django 4.2.6 on 2023-10-22 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_playlist_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlistitem',
            name='playlist',
        ),
        migrations.AlterField(
            model_name='playlistitem',
            name='status',
            field=models.ForeignKey(blank=True, choices=[('To listen', 'To listen'), ('Listened', 'Listened')], null=True, on_delete=django.db.models.deletion.CASCADE, related_name='status', to='core.playlist'),
        ),
    ]
