from django.views.generic import DetailView, ListView,CreateView

from .models import Post

from django.urls import reverse

class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields=[
        "title",
        "body",
        "image",
    ]