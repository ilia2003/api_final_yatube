"""Модуль для отдельных миксинов."""

from rest_framework import viewsets, mixins


class CreateListViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    """Миксины для представлений."""

    pass
