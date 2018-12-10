# standard library
import json

# Django
from django.test import TestCase, Client

# 3rd party
from rest_framework import status

# my stuff here
from .models import (Ingredient)
from .serializers import (IngredientSerializer)

# initialize the APIClient app
client = Client()


class IngredientTest(TestCase):
    """
    Test module for Ingredient model.
    """
    def create_ingredient(self, name="Ingredient Test", is_active=True):
        """
        Create and return object.
        """
        return Ingredient.objects.create(name=name, is_active=is_active)

    def test_ingredient_creation(self):
        ingredient = self.create_ingredient()
        self.assertTrue(isinstance(ingredient, Ingredient))
        self.assertEqual(ingredient.__str__(), ingredient.name)


class GetAllIngredients(TestCase):
    """
    Test API for Ingredient.
    """
    def setUp(self):
        Ingredient.objects.create(name="Ingredient 1", is_active=True)
        Ingredient.objects.create(name="Ingredient 2", is_active=True)
        Ingredient.objects.create(name="Ingredient 3", is_active=True)
        Ingredient.objects.create(name="Ingredient 4", is_active=True)

    def test_get_all_ingredients(self):
        response = client.get('/menu/api/ingredient/')  # get API response

        ingredients = Ingredient.objects.all()  # get data from db
        serializer = IngredientSerializer(ingredients, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
