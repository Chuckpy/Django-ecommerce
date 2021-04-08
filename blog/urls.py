from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("lista", views.PostListView.as_view(), name="list"),
    path("criar/", views.PostCreateView.as_view(), name="create"),
    path("<slug:slug>/", views.PostDetailView.as_view(), name="detail"),    
]