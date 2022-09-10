from django.contrib import admin
from .models import Movie, Review, Todo

# Register your models here.
admin.site.register(Todo)
admin.site.register(Movie)
admin.site.register(Review)



