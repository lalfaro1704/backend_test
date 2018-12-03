# standard libreary
import coreapi
from datetime import datetime

# 3rd-party
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.filters import BaseFilterBackend, OrderingFilter

# my models here
from .models import (Ingredient, Preparation, Lunch)

# my serializers here
from .serializers import (IngredientSerializer, PreparationSerializer, LunchSerializer)

# Create your views here.


class IngredientFilterBackend(BaseFilterBackend):
    """
    Filter for ingredient API.
    """
    def get_schema_fields(self, view):
        return [
            coreapi.Field(
                name='preparation',
                location='query',
                required=False,
                type='str',
                description='Filter ingredients by preparation.',
            ),
        ]

    def filter_queryset(self, request, queryset, view):
        preparation = request.GET.get('preparation', None)
        if preparation:
            return queryset.filter(preparation__id=preparation)
        return queryset


class IngredientViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:
    List all the ingredients of a preparation.
    """
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    filter_backends = [OrderingFilter, IngredientFilterBackend]
    ordering_fields = ('name',)


class PreparationFilterBackend(BaseFilterBackend):
    """
    Filter for preparation API.
    """
    def get_schema_fields(self, view):
        return [
            coreapi.Field(
                name='lunch',
                location='query',
                required=False,
                type='str',
                description='Filter preparations by lunch.',
            ),
        ]

    def filter_queryset(self, request, queryset, view):
        lunch = request.GET.get('lunch', None)
        if lunch:
            return queryset.filter(lunch__id=lunch)
        return queryset


class PreparationViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:
    List all the preparations with all their ingredients.
    """
    queryset = Preparation.objects.all()
    serializer_class = PreparationSerializer
    filter_backends = [OrderingFilter, PreparationFilterBackend]
    ordering_fields = ('name',)


class LunchFilterBackend(BaseFilterBackend):
    """
    Filter for lunch API.
    """
    def get_schema_fields(self, view):
        return [
            coreapi.Field(
                name='menu',
                location='query',
                required=False,
                type='str',
                description='Filter lunches by menu date. Format example: `01-01-2018`.',
            ),
        ]

    def filter_queryset(self, request, queryset, view):
        menu = request.GET.get('menu', None)
        if menu:
            menu = datetime.strptime(menu, '%d-%m-%Y')
            return queryset.filter(menu__date__date=menu.date)
        return queryset.filter(is_active=True)


class LunchViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:
    List all lunches in a menu, by default it returns the active menu of the day.
    """
    queryset = Lunch.objects.all()
    serializer_class = LunchSerializer
    filter_backends = [OrderingFilter, LunchFilterBackend]
    ordering_fields = ('name',)
