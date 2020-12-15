"""View classes of the 'api' app."""
from rest_framework import viewsets, mixins
from rest_framework.pagination import PageNumberPagination

from .models import YamdbUser
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    Viewset for 'users.models.YamdbUser' model.
    """
    queryset = YamdbUser.objects.all()
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination
