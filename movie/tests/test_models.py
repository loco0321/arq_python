from django.test import TestCase

from movie.models import Movie


class MovieTest(TestCase):

    def test_create_movie(self):
        count_movie = Movie.objects.count()
        movie_name = 'Movie 1'
        movie = Movie.objects.create(name=movie_name)
        self.assertEqual(count_movie + 1, Movie.objects.count())
        self.assertEqual(str(movie), movie_name)
