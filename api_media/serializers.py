from django.utils.text import slugify

from rest_framework import serializers

from .models import Categorie


class CategorieSerealizer(serializers.ModelSerializer):
    slug = serializers.SlugField(required=False)

    class Meta:
        fields = ('name', 'slug')
        model = Categorie

    def validate_slug(self, data):
        categorie = Categorie.objects.filter(slug=data).exists()
        if categorie:
            raise serializers.ValidationError(
                {'slug': 'This slug already exists'}
                )
        return data

    def create(self, data):
        if not data.get('slug'):
            data['slug'] = slugify(data.get('name'))
        return super(CategorieSerealizer, self).create(data)
