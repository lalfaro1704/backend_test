# 3rd-party
from rest_framework import viewsets
from rest_framework import mixins

# my models here
from backend_test.menu.models import (Ingredient, Preparation)

# my serializers here
from .serializers import (IngredientSerializer, PreparationSerializer)

# Create your views here.


class IngredientViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:
    List all the ingredients of a preparation.
    """
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class PreparationViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:
    List all the preparations with all their ingredients.
    """
    queryset = Preparation.objects.all()
    serializer_class = PreparationSerializer
