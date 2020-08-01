from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=255)
    director =  models.CharField(max_length=255)
    imdb_score = models.FloatField()
    popularity = models.FloatField()
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.imdb_score = round(self.imdb_score % 10, 1)
        self.popularity = round(self.popularity % 100, 1)
        super(Movie, self).save(*args, **kwargs)