from django.urls import path
from .views import add_movie, delete_movie, filter_movies, add_review, upcoming_screenings, top_movies, add_to_favorites


urlpatterns = [
    path('add_movie/', add_movie, name='add_movie'),
    path('delete_movie/<int:movie_id>/', delete_movie, name='delete_movie'),
    path('filter_movies/', filter_movies, name='filter_movies'),
    path('add_review/<int:movie_id>/', add_review, name='add_review'),
    path('upcoming_screenings/', upcoming_screenings, name='upcoming_screenings'),
    path('top_movies/', top_movies, name='top_movies'),
    path('add_to_favorites/<int:movie_id>/', add_to_favorites, name='add_to_favorites'),
]

