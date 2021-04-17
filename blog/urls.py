from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.PostListView.as_view(), name="list"),
    path("criar/", views.PostCreateView.as_view(), name="create"),
    path("category/<slug:slug>/", views.PostListView.as_view(), name="list_by_category"),
    path("post/<slug:slug>/", views.PostDetailView.as_view(), name="detail"),
    path("favorito/", views.FavoriteView.as_view(), name="favorite"),    
]
