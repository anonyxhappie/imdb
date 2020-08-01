import django_filters
from .models import Movie, Genre


class MovieFilter(django_filters.rest_framework.FilterSet):

    genre = django_filters.CharFilter(field_name='genre__name', lookup_expr='contains')

    class Meta:
        model = Movie
        fields = '__all__'
