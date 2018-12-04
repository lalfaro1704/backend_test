from django.conf.urls import url, include

from rest_framework import routers

from .views import (IngredientViewSet, PreparationViewSet, LunchViewSet, MenuViewSet)


router = routers.DefaultRouter()
router.register(r'ingredient', IngredientViewSet)
router.register(r'preparation', PreparationViewSet)
router.register(r'lunch', LunchViewSet)
router.register(r'menu', MenuViewSet)


urlpatterns = [
    url(r'api/', include(router.urls)),
]
