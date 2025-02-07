"""Разрешения для пользователей."""

from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    """Пользовательский класс для проверок."""

    def has_object_permission(self, request, view, obj):
        """Пользовательская функция для проверок."""
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
