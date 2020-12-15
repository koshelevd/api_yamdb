"""Serializers of the 'users' app."""
from rest_framework import serializers

from .models import YamdbUser


class UserSerializer(serializers.ModelSerializer):
    """
    'ModelSerializer' for 'users.models.YamdbUser' objects.
    """

    class Meta:
        """Adds meta-information."""

        fields = ('first_name', 'last_name', 'username', 'bio', 'email',
                  'role', 'is_admin_role')
        model = YamdbUser
