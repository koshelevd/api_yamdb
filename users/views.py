"""View classes of the 'api' app."""
from rest_framework import viewsets, mixins

from .models import YamdbUser
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    Viewset for 'users.models.YamdbUser' model.
    """

    serializer_class = UserSerializer
