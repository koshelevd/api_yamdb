from django.urls import include, path

from .views import CategoryViewSet, GenreViewSet


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

urlpatterns = [
    path('v1/', include(urlpatterns)),
]
