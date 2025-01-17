from django.db import models

class Movie(models.Model):
    tmdb_id = models.IntegerField(unique=True) 
    title = models.CharField(max_length=255)
    overview = models.TextField()
    release_date = models.DateField()
    poster_path = models.URLField(null=True, blank=True)
    genre = models.CharField(max_length=255, null=True, blank=True)  
    rating = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return self.title

