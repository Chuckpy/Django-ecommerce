from django.views.generic import DetailView, ListView,CreateView

from .models import Post, Comment

from .forms import CreatePostForm

class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    form_class = CreatePostForm


class CommentListView(ListView):
    model = Comment

