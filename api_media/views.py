from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Comment
from .permissions import CustomPermission
from .serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """  A ViewSet for viewing and editing comments."""

    serializer_class = CommentSerializer
    permission_classes = [CustomPermission]
    pagination_class = PageNumberPagination

    def get_queryset(self, *args, **kwargs):
        """  Returns comments of a review."""
        review_id = self.kwargs.get('review_id')
        get_object_or_404(Review, pk=review_id)
        return Comment.objects.filter(review__pk=review_id)

    def perform_create(self, serializer):
        review_id = self.kwargs.get('review_id')
        get_object_or_404(Review, pk=review_id)
        serializer.save(author=self.request.user, review_id=review_id)
