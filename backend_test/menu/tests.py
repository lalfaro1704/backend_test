# Django
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

# my models here
from .models import (Ingredient, Preparation, Lunch, Menu)


class IngredientTest(TestCase):

    def create_ingredient(self, name="Ingredient Test", is_active=True):
        return Ingredient.objects.create(name=name, is_active=is_active)

    def test_ingredient_creation(self):
        ingredient = self.create_ingredient()
        self.assertTrue(isinstance(ingredient, Ingredient))
        self.assertEqual(ingredient.__str__(), ingredient.name)
