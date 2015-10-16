__author__ = 'P057668'

from .models import Music
from .models import Playlist

from django.contrib.auth.models import User


from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    #musics = PlaylistSerializer(many=True, source="Playlist")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'last_login')

    def validate_email(self, attrs, source):
        value = attrs[source]
        if len(value) < 5:
            raise serializers.ValidationError(
                "Text is too short!")
        if value.find("@") == -1:
            raise serializers.ValidationError(
                "Invalid Email!")
        return attrs

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id', 'track_title', 'artist_name', 'album_title', 'cover')

class PlaylistSerializer(serializers.ModelSerializer):
    user = serializers.Field(source='user')
    class Meta:
        model = Playlist
        fields = ('id', 'email', 'track_id', 'added', 'user')


