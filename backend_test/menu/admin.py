# standard library
from django.contrib import admin

# Register your models here.
from .models import (Ingredient, Preparation, Lunch, Menu)


class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    search_fields = ('name',)
    list_filter = ['is_active', ]


class PreparationAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    search_fields = ('name',)
    list_filter = ['is_active', ]
    filter_horizontal = ('recipe',)


class LunchAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    search_fields = ('name',)
    list_filter = ['is_active', ]
    filter_horizontal = ('preparations',)


class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'is_active']
    ordering = ('date',)
    search_fields = ('name',)
    list_filter = ['is_active', ]
    filter_horizontal = ('lunches',)


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Preparation, PreparationAdmin)
admin.site.register(Lunch, LunchAdmin)
admin.site.register(Menu, MenuAdmin)
