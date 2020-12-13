from django.urls import include, path

from .views import CategoryViewSet


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

urlpatterns = [
    path('v1/', include(urlpatterns)),
]
