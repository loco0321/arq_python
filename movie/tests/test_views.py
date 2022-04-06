from django.test import TestCase
from django.urls import reverse_lazy

from movie.models import Movie


class MovieListView(TestCase):

    @classmethod
    def setUpTestData(cls):
        print('cls.setup_test_data_calls')

    def setUp(self):
        print('self.setup_calls')
        Movie.objects.update_or_create(name="MOVIE 1")
        Movie.objects.update_or_create(name="MOVIE 2")

    def test_1_movie_list_is_empty(self):
        Movie.objects.all().delete()
        url = reverse_lazy('movie:movie_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['movie_list']), 0)
        self.assertContains(response, 'No movies to show')

    def test_test1_case_value(self):
        url = reverse_lazy('movie:movie_list')
        response = self.client.get(url, {'name': 'test1'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['result'], 'this is a test')

    def test_list_is_not_empty(self):
        url = reverse_lazy('movie:movie_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['movie_list']), 2)
