from django.urls import path

from users import views as user_views

app_name = "users"

urlpatterns = [
    path("", user_views.profile, name="profile" ),
]