# Generated by Django 4.2.6 on 2023-10-23 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_playlist_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlistitem',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Escutada?'),
        ),
    ]
