from django.db import models

# Create your models here.
class Toys(models.Model):
    toy_name = models.CharField(max_length=35, null=False, unique=True)
    toy_picture = models.ImageField(upload_to="media/")

    def __str__(self): 
        return self.toy_name
