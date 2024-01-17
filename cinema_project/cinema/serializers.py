from rest_framework import serializers
from .models import Movie, Review, Screening, Rating, FavoriteMovie, WatchLater, CreatorBiography


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user_name', 'content']


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'director', 'release_date', 'is_active')


class ScreeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screening
        fields = ['id', 'movie', 'date_time']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'movie', 'value']


class FavoriteMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteMovie
        fields = ['id', 'user', 'movie']
        read_only_fields = ['user']


class WatchLaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchLater
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['movie_title'] = instance.movie.title
        return representation


class CreatorBiographySerializer(serializers.ModelSerializer):
    class Meta:
        model = CreatorBiography
        fields = '__all__'


