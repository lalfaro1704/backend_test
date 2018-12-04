# 3rd-party
from rest_framework import serializers

# my models here
from .models import (Ingredient, Preparation, Lunch, Menu)


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = '__all__'


class PreparationSerializer(serializers.ModelSerializer):
    recipe = IngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Preparation
        fields = '__all__'


class LunchSerializer(serializers.ModelSerializer):
    preparations = PreparationSerializer(many=True, read_only=True)

    class Meta:
        model = Lunch
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    lunches = LunchSerializer(many=True, read_only=True)

    class Meta:
        model = Menu
        fields = '__all__'
