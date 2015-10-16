# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('artist_name', models.CharField(max_length=20)),
                ('track_title', models.CharField(max_length=140)),
                ('album_title', models.CharField(max_length=140)),
                ('cover', models.CharField(max_length=140)),
                ('duration', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('idMusic', models.ForeignKey(to='restapi.Music')),
                ('idUser', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-added'],
            },
        ),
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('email', models.EmailField(max_length=254)),
                ('full_name', models.CharField(blank=True, max_length=120, null=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('modify', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
