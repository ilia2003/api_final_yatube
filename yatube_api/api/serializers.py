"""Сериализаторы для работы с моделями приложения API."""

from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Follow, Group, Post


User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Post."""

    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        """Класс определяет метаданные для сериализатора PostSerializer."""

        fields = ('id', 'text', 'pub_date', 'image', 'author', 'group')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Comment."""

    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        """Класс определяет метаданные для сериализатора CommentSerializer."""

        fields = ('id', 'text', 'created', 'author', 'post')
        model = Comment
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Group."""

    class Meta:
        """Класс определяет метаданные для сериализатора GroupSerializer."""

        fields = ('id', 'title', 'description', 'slug')
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Follow."""

    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        """Класс определяет метаданные для сериализатора FollowSerializer."""

        fields = ('user', 'following')
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('following', 'user'),
                message='Нельзя подписаться еще раз на пользователя'
            )
        ]

    def validate_following(self, value):
        """Функция, где нельзя подписаться на самого себя."""
        if value == self.context['request'].user:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя'
            )
        return value
