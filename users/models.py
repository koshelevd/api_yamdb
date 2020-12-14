"""Contains models to provide an Object-relational Mapping in 'users' app."""
from django.contrib.auth.models import AbstractUser
from django.db import models


class YamdbUser(AbstractUser):
    """
    Extends base 'auth.User' model.
    """

    class UserRoles(models.TextChoices):
        """Enumeration providing user roles."""

        USER = 'user',
        MODERATOR = 'moderator',
        ADMIN = 'admin',

    role = models.CharField(
        max_length=15,
        blank=True,
        choices=UserRoles.choices,
        verbose_name='Роль пользователя'
    )

    class Meta():
        """Adds meta-information."""

        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователь'

