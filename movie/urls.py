from django.urls import path

from movie.views import MovieListView

app_name = 'movie'

urlpatterns = [
    path('list/', MovieListView.as_view(), name='movie_list'),
]
