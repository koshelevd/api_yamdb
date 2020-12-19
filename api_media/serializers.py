from django.utils.text import slugify
from django.db.models import Avg

from rest_framework import serializers

from .models import Category, Comment, Genre, Review, Title


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(required=False)

    class Meta:
        fields = ('name', 'slug')
        model = Category

    def validate_slug(self, data):
        category = Category.objects.filter(slug=data).exists()
        if category:
            raise serializers.ValidationError(
                {'slug': 'This slug already exists'})
        return data

    def create(self, data):
        if not data.get('slug'):
            data['slug'] = slugify(data.get('name'))
        return super(CategorySerializer, self).create(data)


class GenreSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(required=False)

    class Meta:
        fields = ('name', 'slug')
        model = Genre

    def validate_slug(self, data):
        category = Genre.objects.filter(slug=data).exists()
        if category:
            raise serializers.ValidationError(
                {'slug': 'This slug already exists'})
        return data

    def create(self, data):
        if data.get('slug') is None:
            data['slug'] = slugify(data.get('name'))
        return super(GenreSerializer, self).create(data)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault())
    class Meta:
        fields = ('id', 'author', 'text', 'pub_date')
        model = Comment


class TitleSerializer(serializers.ModelSerializer):
    year = serializers.IntegerField(required=False)
    description = serializers.CharField(required=False)
    genre = serializers.SlugRelatedField(many=True,
                                         slug_field='slug',
                                         queryset=Genre.objects.all())
    category = serializers.SlugRelatedField(slug_field='slug',
                                            queryset=Category.objects.all())

    class Meta:
        fields = '__all__'
        model = Title

    def create(self, validated_data):
        genres = validated_data.pop('genre')
        title = Title.objects.create(**validated_data)
        for genre in genres:
            title.genre.add(genre)
        return title

    def to_representation(self, instance):
        representation = super(TitleSerializer,
                               self).to_representation(instance)

        # Present genres in a readable way
        genres_array = []
        for genre in representation['genre']:
            existed_genre = Genre.objects.get(slug=genre)
            dict_genre = {
                'name': existed_genre.name,
                'slug': existed_genre.slug
            }
            genres_array.append(dict_genre)
        representation['genre'] = genres_array

        # present category in a readable way
        category = Category.objects.get(slug=representation['category'])
        dict_category = {'name': category.name, 'slug': category.slug}
        representation['category'] = dict_category

        # add title score in response
        title_reviews = Review.objects.filter(title=instance)
        title_score = title_reviews.aggregate(Avg('score'))
        representation['rating'] = title_score.get('score__avg', 0)
        return representation


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault())
    title = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True,
    )

    class Meta:
        fields = '__all__'
        read_only_fields = ('author', 'title')
        model = Review

    def validate(self, data):
        current_user = self.context['request'].user
        if Review.objects.filter(
                title=self.context['title_id'], author=current_user
        ) and self.context['request'].method == 'POST':
            raise serializers.ValidationError(
                'Вы уже оставляли отзыв на это произведение')
        return data
