from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet

v1_router = DefaultRouter()
v1_router.register(
    r'v1/titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments')

urlpatterns = [
    path('', include(v1_router.urls)),
]
