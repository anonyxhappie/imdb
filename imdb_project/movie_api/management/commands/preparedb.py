import os
import json
from django.db.models import Q
from django.core.management.base import BaseCommand, CommandError
from imdb.settings import TEMP_DIR_LOCATION, JSON_FILE_NAME
from movie_api.models import Movie, Genre

class Command(BaseCommand):
    help = 'Prepares initial DB for project'

    def handle(self, *args, **options):
        # json_path = os.path.join(TEMP_DIR_LOCATION, JSON_FILE_NAME)
        json_path = JSON_FILE_NAME 
        with open(json_path) as f:
            data = json.load(f)
            genre_set = set()
            genre_dict = {}
            movie_list = []
            for _movie in data:
                movie = _movie.copy()
                genres = movie.get('genre', [])
                for g in genres:
                    genre_set.add(g.strip())
                movie['popularity'] = movie['99popularity']
                del movie['99popularity']
                del movie['genre']

                movie_list.append(Movie(**movie))
            
            for genre in list(genre_set):
                stripped_name = genre.strip()
                g, created = Genre.objects.get_or_create(name=stripped_name)
                genre_dict[stripped_name] = g
            
            Movie.objects.bulk_create(movie_list)
            all_movies = Movie.objects.all()
            for i, movie in enumerate(data, start=0):
                genres = []
                for genre in movie.get('genre', []):
                    genres.append(genre_dict[genre.strip()])

                all_movies[i].genre.add(*genres)

        self.stdout.write(self.style.SUCCESS('Data created Successfully'))