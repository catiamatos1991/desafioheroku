from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save



class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=120, blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True, auto_now=False)
    modify = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.email

class Music(models.Model):
    artist_name = models.CharField(max_length=20)
    track_title = models.CharField(max_length=140)
    album_title = models.CharField(max_length=140)
    cover = models.CharField(max_length=140)
    duration = models.CharField(max_length=20)

    db_table ='"music"'

    def __unicode__(self):
        return self.music

class Playlist(models.Model):
    #email = models.CharField(max_length=20)
    idUser = models.ForeignKey(User)
    #track_id = models.CharField(max_length=140)
    idMusic = models.ForeignKey(Music)
    added = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        ordering = ['-added']

    db_table ='"playlist"'


    def __unicode__(self):
        return self.playlist