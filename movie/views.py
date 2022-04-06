from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from movie.models import Movie


class MovieListView(ListView):
    model = Movie

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        value = self.request.GET.get('name')
        if value == 'test1':
            context['result'] = 'this is a test'
        return context
