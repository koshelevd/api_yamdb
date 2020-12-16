from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)


from users.views import UserViewSet
from .views import CategoryViewSet, CommentViewSet, GenreViewSet, ReviewViewSet


users_router = DefaultRouter()
users_router.register('users', UserViewSet)

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
        name='categories_delete'),
    path(
        'genres/',
        GenreViewSet.as_view({
            'get': 'list',
            'post': 'create'}),
        name='genres'),
    path(
        'genres/<slug:slug>/',
        GenreViewSet.as_view({
            'delete': 'destroy'
        }),
        name='genres_delete'),
]


urlpatterns += [
    path('auth/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('', include(users_router.urls))
]

v1_router = DefaultRouter()
v1_router.register(
    r'v1/titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews')
v1_router.register(
    r'v1/titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments')


urlpatterns = [
    path('v1/', include(urlpatterns)),
    path('', include(v1_router.urls)),
]
