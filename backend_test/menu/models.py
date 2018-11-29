# standard library
import uuid

# Django
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel

# Create your models here.


class ActiveAbstract(models.Model):
    """
    Abstract Class. Gives boolean active attribute.
    """
    is_active = models.BooleanField(
        default=True,
        verbose_name=_('is active?')
    )

    class Meta:
        abstract = True


class Ingredient(ActiveAbstract):
    """
    Stores ingredients. Example: `onion`.
    """
    name = models.CharField(
        max_length=150,
        verbose_name=_('name')
    )

    class Meta:
        verbose_name = _('ingredient')
        verbose_name_plural = _('ingredients')

    def __str__(self):
        return "{}".format(self.name)


class Preparation(ActiveAbstract):
    """
    Stores preparations. Example: `hot chicken wings`, `corn`.
    """
    name = models.CharField(
        max_length=500,
        verbose_name=_('name')
    )
    recipe = models.ManyToManyField(
        Ingredient,
        verbose_name=_('recipe')
    )

    class Meta:
        verbose_name = _('preparation')
        verbose_name_plural = _('preparations')

    def __str__(self):
        return "{}".format(self.name)


class Lunch(ActiveAbstract):
    """
    Stores complete lunches. Example: `hot chicken wings, corn and apple pie`.
    """
    name = models.CharField(
        max_length=150,
        verbose_name=_('name')
    )
    preparations = models.ManyToManyField(
        Preparation,
        verbose_name=_('preparations')
    )

    class Meta:
        verbose_name = _('lunch')
        verbose_name_plural = _('lunches')

    def __str__(self):
        return "{}".format(self.name)


class Menu(ActiveAbstract):
    """
    Stores daily menus with some lunches.
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(
        max_length=150,
        verbose_name=_('name')
    )
    lunches = models.ManyToManyField(
        Lunch,
        verbose_name=_('lunches')
    )
    date = models.DateTimeField(
        verbose_name=_('date')
    )

    class Meta:
        verbose_name = _('menu')
        verbose_name_plural = _('menus')

    def __str__(self):
        return "{}".format(self.name)


class Order(TimeStampedModel):
    """
    Stores user orders.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_('user')
    )
    lunch = models.ForeignKey(
        Lunch,
        on_delete=models.CASCADE,
        verbose_name=_('lunch')
    )

    class Meta:
        verbose_name = _('order')
        verbose_name_plural = _('orders')

    def __str__(self):
        return "{} - {}".format(self.user, self.lunch)


class IngredientException(models.Model):
    """
    Stores exceptions of ingredients in a preparation.
    """
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        verbose_name=_('order')
    )
    preparation = models.ForeignKey(
        Preparation,
        on_delete=models.CASCADE,
        verbose_name=_('preparation')
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        verbose_name=_('ingredients')
    )

    class Meta:
        verbose_name = _('exception')
        verbose_name_plural = _('exceptions')

    def __str__(self):
        return "{}".format(self.order)
