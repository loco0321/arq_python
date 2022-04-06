from django.urls import path

from movie.views import MovieListView, MovieDetailView

app_name = 'movie'

urlpatterns = [
    path('list/', MovieListView.as_view(), name='movie_list'),
    path('detail/<slug:pk>/', MovieDetailView.as_view(), name='movie_detail'),
]
