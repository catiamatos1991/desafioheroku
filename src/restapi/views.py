from django.contrib.auth.models import User
from django.shortcuts import render_to_response, render

from .models import Music
from .models import Playlist

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from restapi.serializers import UserSerializer
from restapi.serializers import MusicSerializer
from restapi.serializers import PlaylistSerializer

from django.http import Http404

from .forms import SignUpForm

def index(request):
    title = "Welcome %s" %(request.user)
    context = {
        "title": "thank you"
    }
    return render(request, "index.html", context)
    #add a form
    # if request.method == 'POST':
    #     form = SignUpForm(request.POST or None)
    #     context = {
    #         "title": title,
    #         "form": form
    #     }
    #
    # if form.is_valid():
    #     instance = form.save(commit=False)
    #     full_name = form.cleaned_date.get("full_name")
    #     if not full_name:
    #         full_name = "New full name"
    #     instance.full_name = full_name
    #     instance.save()


def login(request):
    context = {

    }
    return render(request, "login.html", context)

def artists(request):
    return render_to_response("artists.html")

def home(request):
    if request.user.is_authenticated():
        user = request.user
    context = {
        "user": user
    }
    return render(request, "home.html", context)

def musics(request):
    return render_to_response("musics.html")

def playlist(request):
    return render_to_response("playlist.html")

class UserList(APIView):
    """
    List all users, or create a new user.
    """
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        user = UserSerializer(user)
        return Response(user.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class MusicList(APIView):
    """
    List all musics, or create a new music.
    """
    def get(self, request, format=None):
        musics = Music.objects.all()
        serializer = MusicSerializer(musics, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MusicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        musics = self.get_object(pk)
        musics.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class MusicDetail(APIView):
    """
    Retrieve, update or delete a music instance.
    """
    def get_object(self, pk):
        try:
            return Music.objects.get(pk=pk)
        except Music.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        musics = self.get_object(pk)
        musics = MusicSerializer(musics)
        return Response(musics.data)

    def put(self, request, pk, format=None):
        musics = self.get_object(pk)
        serializer = MusicSerializer(musics, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        musics = self.get_object(pk)
        musics.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class PlaylistList(APIView):
    """
    List all playlists, or create a new playlist.
    """
    def get(self, request, format=None):
        pl = Playlist.objects.all()
        serializer = PlaylistSerializer(pl, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PlaylistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        pl = self.get_object(pk)
        pl.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PlaylistDetail(APIView):
    """
    Retrieve, update or delete a playlist instance.
    """
    def get_object(self, pk):
        try:
            return Playlist.objects.get(pk=pk)
        except Playlist.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        playlist = self.get_object(pk)
        playlist = PlaylistSerializer(playlist)
        return Response(playlist.data)

    def put(self, request, pk, format=None):
        playlist = self.get_object(pk)
        serializer = PlaylistSerializer(playlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        playlist = self.get_object(pk)
        playlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        #### View Sets ...


class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly)

class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def pre_save(self, obj):
        obj.user = self.request.user