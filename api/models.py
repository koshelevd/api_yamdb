"""Contains models to provide an Object-relational Mapping in 'api' app."""
from django.db import models


class Category(models.Model):
    """
    Stores a single category entry.
    """

    name = models.CharField(
        max_length=200,
        verbose_name='Название',
    )
    slug = models.SlugField(
        max_length=250,
        unique=True,
        null=True,
        verbose_name='ЧПУ',
    )

    class Meta():
        """Adds meta-information."""

        verbose_name_plural = 'Категории произведений'
        verbose_name = 'Категория'

    def __str__(self):
        """Return category info."""
        return (f'Category "{self.name[:50]}", '
                f'slug="{self.slug[:50]}"')


class Genre(models.Model):
    """
    Stores a single genre entry.
    """

    name = models.CharField(
        max_length=200,
        verbose_name='Название',
    )
    slug = models.SlugField(
        max_length=250,
        unique=True,
        null=True,
        verbose_name='ЧПУ',
    )

    class Meta():
        """Adds meta-information."""

        verbose_name_plural = 'Жанры произведений'
        verbose_name = 'Жанр'

    def __str__(self):
        """Return genre info."""
        return (f'Genre "{self.name[:50]}", '
                f'slug="{self.slug[:50]}"')
