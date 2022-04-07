from django.contrib import admin

# Register your models here.
from movie.models import Movie, Currency


class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'score')


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('code', 'value', 'created_at')


admin.site.register(Movie, MovieAdmin)
admin.site.register(Currency, CurrencyAdmin)
