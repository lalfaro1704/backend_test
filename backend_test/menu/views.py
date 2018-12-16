# standard library
import coreapi
from datetime import datetime

# Django
from django.contrib.auth import get_user_model
from django.db import transaction
from django.utils.translation import ugettext_lazy as _

# 3rd-party
from rest_framework import viewsets, status
from rest_framework import mixins
from rest_framework.filters import BaseFilterBackend, OrderingFilter
from rest_framework.response import Response

# my models here
from .models import (Ingredient, Preparation, Lunch, Menu, Order, IngredientException)

# my serializers here
from .serializers import (IngredientSerializer, PreparationSerializer, LunchSerializer, MenuSerializer,
                          OrderSerializer)

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


class MenuFilterBackend(BaseFilterBackend):
    """
    Filter for menu API.
    """
    def get_schema_fields(self, view):
        return [
            coreapi.Field(
                name='date',
                location='query',
                required=False,
                type='str',
                description='Filter menu by date. Format example: `01-01-2018`.',
            ),
        ]

    def filter_queryset(self, request, queryset, view):
        date = request.GET.get('date', None)
        if date:
            date = datetime.strptime(date, '%d-%m-%Y')
            return queryset.filter(date__date=date)
        return queryset.filter(is_active=True)


class MenuViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
    Daily menu!.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    filter_backends = [MenuFilterBackend]


class OrderViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    create:
    Store order for menu.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request):
        user = request.data.get('user', None)
        lunch = request.data.get('lunch', None)
        exclutions = request.data.get('exclutions', [])
        errors = {}

        try:
            user = get_user_model().objects.get(username=user)
        except get_user_model().DoesNotExist:
            errors['errors'] = _("Invalid user!")
            return Response(errors, status=status.HTTP_404_NOT_FOUND)

        try:
            with transaction.atomic():
                order = Order.objects.create(
                    user=user,
                    lunch=Lunch.objects.get(id=lunch)
                )

                for exclution in exclutions:
                    ingredient_exception = IngredientException.objects.create(
                        order=order,
                        preparation=Preparation.objects.get(id=exclution['id_preparation'])
                    )
                    for ingredient in exclution['ingredients']:
                        ingredient = Ingredient.objects.get(id=ingredient)
                        ingredient_exception.ingredients.add(ingredient)
                serializer = self.serializer_class(order)

                return Response(
                    data=serializer.data,
                    status=status.HTTP_201_CREATED
                )
        except Exception as e:
            errors['errors'] = e

        return Response(errors, status=status.HTTP_400_BAD_REQUEST)
