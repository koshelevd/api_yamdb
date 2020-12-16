"""View classes of the 'api' app."""
from uuid import uuid4

from django.db.utils import IntegrityError
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.exceptions import ParseError, APIException
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .models import YamdbUser
from .serializers import UserSerializer
from .permissions import IsAdmin


class UserViewSet(viewsets.ModelViewSet):
    """
    Viewset for 'users.models.YamdbUser' model.
    """

    queryset = YamdbUser.objects.all().order_by('id')
    lookup_field = 'username'
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination
    permission_classes = (IsAdmin,)

    @action(detail=False,
            methods=('get', 'patch'),
            permission_classes=(IsAuthenticated,))
    def me(self, request):
        serializer = UserSerializer(
            request.user,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def auth_email(request):
    """

    :param request:
    :return:
    """
    try:
        email = request.data.get('email')
        username = email.split('@')[0]
        obj, created = YamdbUser.objects.get_or_create(
            username=username,
            email=email,
            confirmation_code=str(uuid4())
        )
    except AttributeError:
        raise ParseError
    except IntegrityError:
        raise BadRequest
    except:
        raise ServerError

    return Response({"message": "Hello, world!"})


class BadRequest(APIException):
    status_code = 400
    default_detail = 'Bad request.'

class ServerError(APIException):
    status_code = 500
    default_detail = 'Internal server error.'
