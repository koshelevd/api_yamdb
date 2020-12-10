"""Application 'api' admin page configuration."""
from django.contrib import admin

from .models import Category, Comment, Genre, Review, Title


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Manage categories."""

    list_display = (
        'pk',
        'name',
        'slug',
    )
    search_fields = (
        'name',
        'slug',
    )
    empty_value_display = '-пусто-'
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Manage genres."""

    list_display = (
        'pk',
        'name',
        'slug',
    )
    search_fields = (
        'name',
        'slug',
    )
    empty_value_display = '-пусто-'
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Manage comments."""

    list_display = (
        'pk',
        'review',
        'text',
        'author',
        'pub_date',
    )
    list_filter = ('pub_date',)
    search_fields = (
        'text',
    )
    empty_value_display = '-пусто-'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Manage reviews."""

    list_display = (
        'pk',
        'title',
        'text',
        'author',
        'score',
        'pub_date',
    )
    list_filter = ('pub_date', 'score')
    search_fields = (
        'text',
    )
    empty_value_display = '-пусто-'


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    """Manage titles."""

    list_display = (
        'pk',
        'name',
        'year',
        'category',
        'genres'
    )
    list_filter = ('year',)
    search_fields = (
        'name',
    )
    empty_value_display = '-пусто-'