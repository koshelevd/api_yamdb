from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, CommentViewSet

urlpatterns = [
    path(
        'categories/',
        CategoryViewSet.as_view({
            'get': 'list',
            'post': 'create'}),
        name='categories'),
    path(
        'categories/<slug:slug>/',
        CategoryViewSet.as_view({
            'delete': 'destroy'
        }),
        name='categories'),
]

v1_router = DefaultRouter()
v1_router.register(
    r'v1/titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments')

urlpatterns = [
    path('v1/', include(urlpatterns)),
    path('', include(v1_router.urls)),
]
