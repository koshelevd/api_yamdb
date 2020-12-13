from django.shortcuts import get_object_or_404, render
from rest_framework import status, filters, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Categorie
from .permissions import IsGetOrIsAdmin
from .serializers import CategorieSerealizer


class CategorieViewSet(viewsets.ModelViewSet):
    model = Categorie
    queryset = Categorie.objects.all().order_by('name')
    serializer_class = CategorieSerealizer
    permission_classes = [IsGetOrIsAdmin]
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ('name',)

    def destroy(self, request, *args, **kwargs):
        categorie = get_object_or_404(Categorie, slug=kwargs['slug'])
        categorie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)