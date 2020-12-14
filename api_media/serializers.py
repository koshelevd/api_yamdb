from rest_framework import serializers

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        field = '__all__'
        read_only_fields = 'author', 'review', 'title'
        model = Comment
