from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

class Todo(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)

    #sets time when todo object is made
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=True)

    #user who made the todo
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title 
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'movie_{0}/{1}'.format(instance.Movie.title, filename)
class Movie(models.Model):
    movie_cover = models.FileField(upload_to='user_directory_path', default='default.jpg')
    title = models.CharField(max_length=100)
    genres = TaggableManager()
    plot = models.TextField(blank=True)
    suggested_by = models.ForeignKey(User, on_delete=models.CASCADE)
    suggested_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title 


class Review(models.Model):
    author = models.CharField(max_length=40, default="anonymous")
    review_date = models.DateTimeField(default=timezone.now)
    rate_choices = (
        (1,1),
        (1.5,1.5),
        (2,2),
        (2.5,2.5),
        (3,3),
        (3.5,3.5),
        (4,4),
        (4.5,4.5),
        (5,5)
    )
    stars = models.IntegerField(choices=rate_choices)
    comment = models.TextField(max_length=4000)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
