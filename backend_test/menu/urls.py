from django.conf.urls import url, include

from rest_framework import routers

from .views import (IngredientViewSet)

router = routers.DefaultRouter()
router.register(r'ingredients', IngredientViewSet)

urlpatterns = [
    url(r'api/', include(router.urls)),
]
