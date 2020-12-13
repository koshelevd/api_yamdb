from django.utils.text import slugify

from rest_framework import serializers

from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(required=False)

    class Meta:
        fields = ('name', 'slug')
        model = Category

    def validate_slug(self, data):
        category = Category.objects.filter(slug=data).exists()
        if category:
            raise serializers.ValidationError(
                {'slug': 'This slug already exists'}
                )
        return data

    def create(self, data):
        if not data.get('slug'):
            data['slug'] = slugify(data.get('name'))
        return super(CategorySerializer, self).create(data)
