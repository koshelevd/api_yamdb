from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Comment(models.Model):
    """Creates a 'model.Comment' object for a 'model.Review' object"""
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='comments')
    title = models.ForeignKey(Title,
                              on_delete=models.CASCADE,
                              related_name='+')
    review = models.ForeignKey(Review,
                               on_delete=models.CASCADE,
                               related_name='comments')
    text = models.TextField()
    created = models.DateField('Дата добавления',
                               auto_now_add=True,
                               db_index=True)
