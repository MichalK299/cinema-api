from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.utils import timezone
from .models import Movie, Review, Screening, Rating, FavoriteMovie
from .serializers import MovieSerializer, ReviewSerializer, ScreeningSerializer, RatingSerializer, FavoriteMovieSerializer
from django.shortcuts import get_object_or_404
from django.db import models
from rest_framework import permissions, status
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(
    method='post',
    request_body=MovieSerializer,
    responses={201: 'Movie added successfully', 400: 'Invalid data'},
    operation_description='Add a new movie'
)
@api_view(['POST'])
def add_movie(request):
    serializer = MovieSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='delete',
    responses={200: 'Movie deleted successfully', 404: 'Movie not found'},
    operation_description='Delete a movie by ID'
)
@api_view(['DELETE'])
def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    movie.delete()
    return Response({'message': 'Movie deleted successfully'})


@api_view(['GET'])
def filter_movies(request):
    title = request.GET.get('title', '')
    director = request.GET.get('director', '')
    release_date = request.GET.get('release_date', '')

    movies = Movie.objects.filter(
        title__icontains=title,
        director__icontains=director,
        release_date__icontains=release_date
    )

    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@swagger_auto_schema(
    method='post',
    request_body=ReviewSerializer,
    responses={200: 'Review added successfully', 400: 'Invalid data'},
    operation_description='Add a review for a movie'
)
@api_view(['POST'])
def add_review(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    serializer = ReviewSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(movie=movie)
        return Response({'message': 'Review added successfully'})
    else:
        return Response(serializer.errors, status=400)


@api_view(['GET'])
def upcoming_screenings(request):
    current_datetime = timezone.now()
    upcoming_screenings = Screening.objects.filter(date_time__gte=current_datetime).order_by('date_time')[:5]

    serializer = ScreeningSerializer(upcoming_screenings, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def top_movies(request):
    top_movies = Movie.objects.annotate(avg_rating=models.Avg('ratings__value')).order_by('-avg_rating')[:5]

    serializer = MovieSerializer(top_movies, many=True)
    return Response(serializer.data)


@swagger_auto_schema(
    method='post',
    responses={200: 'Movie added to favorites successfully', 400: 'Invalid data'},
    operation_description='Add a movie to favorites'
)
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def add_to_favorites(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    favorite_movie, created = FavoriteMovie.objects.get_or_create(user=request.user, movie=movie)

    if created:
        return Response({'message': f'{movie.title} added to favorites'})
    else:
        return Response({'message': f'{movie.title} is already in favorites'})


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def user_favorite_movies(request):
    user_favorite_movies = FavoriteMovie.objects.filter(user=request.user)
    serializer = FavoriteMovieSerializer(user_favorite_movies, many=True)
    return Response(serializer.data)
