# standard libreary
import coreapi

# 3rd-party
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.filters import BaseFilterBackend, OrderingFilter

# my models here
from backend_test.menu.models import (Ingredient, Preparation)

# my serializers here
from .serializers import (IngredientSerializer, PreparationSerializer)

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
    ordering_fields = ('name', '-name',)


class PreparationViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:
    List all the preparations with all their ingredients.
    """
    queryset = Preparation.objects.all()
    serializer_class = PreparationSerializer
