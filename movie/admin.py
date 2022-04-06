from django.contrib import admin

# Register your models here.
from movie.models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'score')


admin.site.register(Movie, MovieAdmin)
