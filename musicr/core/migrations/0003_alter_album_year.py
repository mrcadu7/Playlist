# Generated by Django 4.2.6 on 2023-10-24 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_album_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='year',
            field=models.DateField(blank=True, null=True),
        ),
    ]
