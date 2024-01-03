from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    release_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    user_name = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return f'{self.user_name}\'s review for {self.movie.title}'


class Screening(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date_time = models.DateTimeField()

    def __str__(self):
        return f'Screening of {self.movie.title} at {self.date_time}'


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return f'Rating of {self.movie.title}: {self.value}'


class FavoriteMovie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}\'s favorite: {self.movie.title}'
