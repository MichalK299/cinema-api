from django.contrib import admin
from .models import Movie, Review, Screening, Rating, FavoriteMovie, WatchLater, CreatorBiography

admin.site.register(Movie)
admin.site.register(CreatorBiography)
admin.site.register(WatchLater)
admin.site.register(Review)
admin.site.register(Screening)
admin.site.register(Rating)
admin.site.register(FavoriteMovie)
