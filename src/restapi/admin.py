from django.contrib import admin
from restapi.forms import SignUpForm
from restapi.models import SignUp, Music, Playlist

# Register your models here.
class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "added", "modify"]
    form = SignUpForm

class MusicAdmin(admin.ModelAdmin):
    pass

class PlaylistAdmin(admin.ModelAdmin):
    pass

admin.site.register(SignUp, SignUpAdmin)
admin.site.register(Music, MusicAdmin)
admin.site.register(Playlist, PlaylistAdmin)

