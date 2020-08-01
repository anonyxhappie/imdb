from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django_filters import rest_framework as filters

from .models import Movie
from .filters import MovieFilter
from .serializers import MovieSerializer
from .permissions import CustomPermission

class MovieViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing movie instances.
    """

    permission_classes = [CustomPermission]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = MovieFilter
    filterset_fields = ('name', 'director', 'imdb_score', 'popularity', 'genre')

    def list(self, request):

        # with filter
        queryset = self.filter_queryset(self.get_queryset())

        # pagination
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            output_data = serializer.data
            for movie in output_data:
                movie = self.update_genre_data_structure(movie)

            return self.get_paginated_response(output_data)

        serializer = self.get_serializer(queryset, many=True)
        
        output_data = serializer.data
        for movie in output_data:
            movie = self.update_genre_data_structure(movie)
        return Response(output_data)

    def retrieve(self, request, pk=None):
        movie = get_object_or_404(self.queryset, pk=pk)
        serializer = MovieSerializer(movie)
        output_data = serializer.data
        output_data = self.update_genre_data_structure(output_data)
        return Response(output_data)
    
    def update_genre_data_structure(self, movie):
        genre_list = []
        for g in movie['genre']:
            genre_list.append(g['name'])
        movie['genre'] = genre_list
        return movie