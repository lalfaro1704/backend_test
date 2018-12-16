from django.conf.urls import url, include

from rest_framework import routers

from .views import (IngredientViewSet, PreparationViewSet, LunchViewSet, MenuViewSet, OrderViewSet)


router = routers.DefaultRouter()
router.register(r'ingredient', IngredientViewSet)
router.register(r'preparation', PreparationViewSet)
router.register(r'lunch', LunchViewSet)
router.register(r'menu', MenuViewSet)
router.register(r'order', OrderViewSet)


urlpatterns = [
    url(r'api/', include(router.urls)),
]
