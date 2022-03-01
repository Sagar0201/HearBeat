# Generated by Django 4.0 on 2022-02-21 12:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('beat', '0015_delete_favourites'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavouritesSongs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorited_by', models.ManyToManyField(related_name='favorite_songs', to=settings.AUTH_USER_MODEL)),
                ('song', models.ManyToManyField(related_name='favorite_songs', to='beat.Songs')),
            ],
        ),
    ]
