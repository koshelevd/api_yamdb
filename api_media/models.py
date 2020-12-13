from django.db import models


class Categorie(models.Model):
    ''' Categorie model represents different types of media with can be
    reviewed, e.g. movies, books, etc '''
    name = models.CharField(
        max_length=20,
        null=False,
        unique=True,
        )
    slug = models.SlugField(
        max_length=20,
        null=False,
        unique=True,
        )

    def __str__(self):
        return self.name
