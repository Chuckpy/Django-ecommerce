from django.urls import path

from .views import OrderCreateView

app_name = "orders"

urlpatterns = [
    path("criar/", OrderCreateView.as_view(), name="criar"),
]