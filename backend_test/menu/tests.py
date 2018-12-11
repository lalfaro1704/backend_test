# standard library
from datetime import datetime

# Django
from django.test import TestCase, Client

# 3rd party
from rest_framework import status

# my stuff here
from .models import (Ingredient, Preparation, Lunch, Menu)
from .serializers import (IngredientSerializer, PreparationSerializer, MenuSerializer)

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


class GetAllPreparations(TestCase):
    """
    Test API for Preparation.
    """
    def setUp(self):
        i1 = Ingredient.objects.create(name="Ingredient 1", is_active=True)
        i2 = Ingredient.objects.create(name="Ingredient 2", is_active=True)
        i3 = Ingredient.objects.create(name="Ingredient 3", is_active=True)
        i4 = Ingredient.objects.create(name="Ingredient 4", is_active=True)
        p1 = Preparation.objects.create(name="Preparation 1", is_active=True)
        p2 = Preparation.objects.create(name="Preparation 2", is_active=True)
        p1.recipe.add(i1, i2)
        p2.recipe.add(i3, i4)

    def test_get_all_ingredients(self):
        response = client.get('/menu/api/preparation/')  # get API response

        preparations = Preparation.objects.all()  # get data from db
        serializer = PreparationSerializer(preparations, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetAllMenus(TestCase):
    """
    Test API for Menus.
    """
    def setUp(self):
        i1 = Ingredient.objects.create(name="Ingredient 1", is_active=True)
        i2 = Ingredient.objects.create(name="Ingredient 2", is_active=True)
        i3 = Ingredient.objects.create(name="Ingredient 3", is_active=True)
        i4 = Ingredient.objects.create(name="Ingredient 4", is_active=True)
        p1 = Preparation.objects.create(name="Preparation 1", is_active=True)
        p2 = Preparation.objects.create(name="Preparation 2", is_active=True)
        p1.recipe.add(i1, i2)
        p2.recipe.add(i3, i4)
        l1 = Lunch.objects.create(name="Lunch 1", is_active=True)
        l2 = Lunch.objects.create(name="Lunch 2", is_active=True)
        l1.preparations.add(p1)
        l2.preparations.add(p2)
        menu = Menu.objects.create(name="Menu 1", date=datetime.now())
        menu.lunches.add(l1, l2)

    def test_get_all_ingredients(self):
        response = client.get('/menu/api/menu/')  # get API response

        menus = Menu.objects.all()  # get data from db
        serializer = MenuSerializer(menus, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
