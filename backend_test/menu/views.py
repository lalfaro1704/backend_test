# 3rd-party
from rest_framework import viewsets
from rest_framework import mixins

# my models here
from backend_test.menu.models import (Ingredient)

# my serializers here
from .serializers import (IngredientSerializer)

# Create your views here.


class IngredientViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:
    List all the ingredients of a recipe.
    """
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
