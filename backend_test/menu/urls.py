from django.conf.urls import url, include

from rest_framework import routers

from .views import (IngredientViewSet, PreparationViewSet, LunchViewSet)


router = routers.DefaultRouter()
router.register(r'ingredient', IngredientViewSet)
router.register(r'preparation', PreparationViewSet)
router.register(r'lunch', LunchViewSet)


urlpatterns = [
    url(r'api/', include(router.urls)),
]
