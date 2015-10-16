"""desafio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""


from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from rest_framework.routers import DefaultRouter

from restapi import views
admin.autodiscover()

router = DefaultRouter()
router.register(r'music', views.MusicViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'playlist', views.PlaylistViewSet)


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^music/$', views.MusicList.as_view()),
    url(r'^music/(?P<pk>[0-9]+)/$', views.MusicDetail.as_view()),
    url(r'^playlist/$', views.PlaylistList.as_view()),
    url(r'^playlist/(?P<pk>[0-9]+)/$', views.PlaylistDetail.as_view()),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^artists/$', views.artists, name='artists'),
    url(r'^home/$', views.home, name='home'),
    url(r'^musics/$', views.musics, name='musics'),
    url(r'^myplaylist/$', views.playlist, name='myplaylist'),
    url(r'^manage', views.manage, name='manage'),
    ]

#if settings.DEBUG:
   # urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
   # urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)