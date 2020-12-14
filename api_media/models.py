from django.contrib.auth import get_user_model
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
