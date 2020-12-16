from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

User = get_user_model()


class Category(models.Model):
    """ Category model represents different types of media with can be
    reviewed, e.g. movies, books, etc """
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


class Genre(models.Model):
    """ Genre model represents different types of genres """
    name = models.CharField(
        max_length=30,
        null=False,
        unique=True,
        verbose_name='Название жанра',
    )
    slug = models.SlugField(
        max_length=30,
        null=False,
        unique=True,
    )

    def __str__(self):
        return self.name


class Review(models.Model):
    """ Creates a 'model.Review' object for a 'model.Title' object"""
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    review_title = models.TextField()
    text = models.TextField()
    created = models.DateField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True,
    )
    score = models.IntegerField(
        validators=[MinValueValidator(1),
                    MaxValueValidator(10)])


class Comment(models.Model):
    """Creates a 'model.Comment' object for a 'model.Review' object"""
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='+',
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    text = models.TextField()
    created = models.DateField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True,
    )
