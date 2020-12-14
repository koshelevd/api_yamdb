"""Contains models to provide an Object-relational Mapping in 'users' app."""
from django.contrib.auth.models import AbstractUser
from django.db import models


class YamdbUser(AbstractUser):
    """
    Extends base 'auth.User' model.
    """

    ROLES = (
        'user',
        'moderator',
        'admin',
    )
    role = models.CharField(
        max_length=15,
        blank=True,
        choices=ROLES)
