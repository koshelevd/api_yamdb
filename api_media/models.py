from django.db import models


class Category(models.Model):
    ''' Category model represents different types of media with can be
    reviewed, e.g. movies, books, etc '''
    name = models.CharField(
        max_length=30,
        null=False,
        unique=True,
        verbose_name='Название категории',
        )
    slug = models.SlugField(
        max_length=30,
        null=False,
        unique=True,
        )

    def __str__(self):
        return self.name
