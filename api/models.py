"""Contains models to provide an Object-relational Mapping in 'api' app."""
from django.db import models


class Category(models.Model):
    """
    Stores a single category entry.
    """

    name = models.CharField(
        max_length=200,
        verbose_name='Название',
    )
    slug = models.SlugField(
        max_length=250,
        unique=True,
        null=True,
        verbose_name='ЧПУ',
    )

    class Meta():
        """Adds meta-information."""

        verbose_name_plural = 'Категории произведений'
        verbose_name = 'Категория'

    def __str__(self):
        """Return category info."""
        return (f'Category "{self.name[:50]}", '
                f'slug="{self.slug[:50]}"')


class Genre(models.Model):
    """
    Stores a single genre entry.
    """

    name = models.CharField(
        max_length=200,
        verbose_name='Название',
    )
    slug = models.SlugField(
        max_length=250,
        unique=True,
        null=True,
        verbose_name='ЧПУ',
    )

    class Meta():
        """Adds meta-information."""

        verbose_name_plural = 'Жанры произведений'
        verbose_name = 'Жанр'

    def __str__(self):
        """Return genre info."""
        return (f'Genre "{self.name[:50]}", '
                f'slug="{self.slug[:50]}"')


class Title(models.Model):
    """
    Stores a single title entry.
    """

    name = models.CharField(
        max_length=200,
        verbose_name='Название',
    )
    year = models.DecimalField(
        max_digits=4,
        null=True,
        verbose_name='Год выпуска',
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='titles',
        verbose_name='Категория',
    )
    genres = models.ManyToManyField(
        'Genre',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='titles',
        verbose_name='Жанры',
    )

    class Meta():
        """Adds meta-information."""

        verbose_name_plural = 'Произведения'
        verbose_name = 'Произведение'

    def __str__(self):
        """Return title's info."""
        return (f'Title "{self.name[:50]}", '
                f'year "{self.year}"')


class Review(models.Model):
    """
    Stores a single review entry.
    """

    title = models.ForeignKey(
        'Title',
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение',
    )
    text = models.TextField(
        verbose_name='Содержание отзыва',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор',
    )
    score = models.DecimalField(
        max_digits=2,
        verbose_name='Оценка',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
    )

    class Meta():
        """Adds meta-information."""

        verbose_name_plural = 'Отзывы'
        verbose_name = 'Отзыв'

    def __str__(self):
        """Return review's info."""
        return (f'Author "{self.author}", title "{self.title}", '
                f'text "{self.text[:50]}", date "{self.pub_date}"')
