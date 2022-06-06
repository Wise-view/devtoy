from django.db import models

# Create your models here.
class Forms(models.Model):
    album_name = models.CharField(max_length=35, null=False, unique=True)
    artist_name = models.CharField(max_length=35, null=False, unique=True)
    album_picture = models.ImageField(upload_to="media/")

    def __str__(self): 
        return self.artist_name
