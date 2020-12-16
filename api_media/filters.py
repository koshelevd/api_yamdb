import django_filters

from .models import Title


class TitleFilter(django_filters.FilterSet):

    class Meta:
        model = Title
        fields = [
            'category',
            'genre',
            'name',
            'year',
            ]