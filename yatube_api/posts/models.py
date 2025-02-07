"""Классы для работы с API."""

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    """Класс для создания группы."""

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        """Функция для описания класса."""
        return self.title


class Post(models.Model):
    """Класс для создания поста."""

    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='posts'
    )
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)

    def __str__(self):
        """Функция для описания класса."""
        return self.text


class Comment(models.Model):
    """Класс для создания комментария."""

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    def __str__(self):
        """Функция для описания класса."""
        return self.text


class Follow(models.Model):
    """Класс для создания пользователей,."""

    """которые могут подписываться друг на друга."""

    following = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='following',
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='follower'
    )

    class Meta:
        """Класс определяет метаданные для модели Follow."""

        constraints = [
            models.CheckConstraint(
                name='%(app_label)s_%(class)s_prevent_self_follow',
                check=~models.Q(user=models.F('following')),
            ),
            models.UniqueConstraint(
                fields=['following', 'user'],
                name='%(app_label)s_%(class)s_unique_relationships'
            )
        ]
