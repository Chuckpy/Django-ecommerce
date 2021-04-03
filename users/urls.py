from django.urls import path

from .views import CreateUser

app_name = "cadastro"

urlpatterns = [
    path("cadastro/", CreateUser.as_view(), name="cadastro")
]