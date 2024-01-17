from django.urls import path, include
from .views import *
from . import views


urlpatterns = [
    path('add_movie/', views.add_movie, name='add_movie'),
    path('delete_movie/<int:movie_id>/', delete_movie, name='delete_movie'),
    path('filter_movies/', filter_movies, name='filter_movies'),
    path('add_review/<int:movie_id>/', add_review, name='add_review'),
    path('upcoming_screenings/', upcoming_screenings, name='upcoming_screenings'),
    path('top_movies/', top_movies, name='top_movies'),
    path('add_to_favorites/<int:movie_id>/', add_to_favorites, name='add_to_favorites'),
    path('add_to_watch_later/<int:movie_id>/', add_to_watch_later, name='add_to_watch_later'),
    path('remove_from_watch_later/<int:movie_id>/', remove_from_watch_later, name='remove_from_watch_later'),
    path('add_creator_biography/', add_creator_biography, name='add_creator_biography'),
    path('edit_creator_biography/<int:biography_id>/', edit_creator_biography, name='edit_creator_biography'),
    path('delete_creator_biography/<int:biography_id>/', delete_creator_biography, name='delete_creator_biography'),

]

