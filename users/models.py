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
        default=UserRoles.USER,
        verbose_name='Роль пользователя'
    )
    bio = models.TextField(
        null=True,
        verbose_name='Описание',
    )

    class Meta():
        """Adds meta-information."""

        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователь'

    @property
    def is_user(self):
        """Return True if user's role equals 'user'."""
        return self.role == 'user'

    @property
    def is_moderator(self):
        """Return True if user's role equals 'moderator'."""
        return self.role == 'moderator'

    @property
    def is_admin(self):
        """Return True if user is superuser or role equals 'admin'."""
        return self.role == 'admin' or self.is_superuser
