"""Serializers of the 'users' app."""
from rest_framework import serializers

from .models import YamdbUser


class UserSerializer(serializers.ModelSerializer):
    """
    'ModelSerializer' for 'users.models.YamdbUser' objects.
    """

    class Meta:
        """Adds meta-information."""

        fields = '__all__'
        model = YamdbUser
