from django.urls import include, path

from .views import CategorieViewSet


urlpatterns = [
    path(
        'categories/',
        CategorieViewSet.as_view({
            'get': 'list',
            'post': 'create'}),
        name='categories'),
    path(
        'categories/<slug:slug>/',
        CategorieViewSet.as_view({
            'delete': 'destroy'
        }),
        name='categories'),
]

urlpatterns = [
    path('v1/', include(urlpatterns)),
]
