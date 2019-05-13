from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator

class Gener(models.Model):
    name = models.CharField(max_length=140,unique=True)


    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=140)
    gener = models.ManyToManyField(Gener)
    imdb_score = models.IntegerField(default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]

    )
    popularity = models.FloatField(default=1,
        validators=[
            MaxValueValidator(100.0),
            MinValueValidator(1)
        ]
    )
    director = models.CharField(max_length=140)
    #genre = ArrayField(models.CharField(max_length=200), blank=True)


    def __str__(self):
        return self.name




# Create your models here.
