# 3rd-party
from rest_framework import serializers

# my models here
from backend_test.menu.models import (Ingredient, Preparation)


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = '__all__'


class PreparationSerializer(serializers.ModelSerializer):
    recipe = IngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Preparation
        fields = '__all__'
