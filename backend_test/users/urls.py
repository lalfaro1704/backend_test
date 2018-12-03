from django.urls import path

from backend_test.users.views import (user_list_view, user_detail_view)

app_name = "users"
urlpatterns = [
    path("", view=user_list_view, name="list"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
