# 3rd-party
from rest_framework import serializers

# my models here
from backend_test.menu.models import (Ingredient)


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = '__all__'
