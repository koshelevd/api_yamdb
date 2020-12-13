from rest_framework import serializers

from .models import Categorie


class CategorieSerealizer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug')
        model = Categorie