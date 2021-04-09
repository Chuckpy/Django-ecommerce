from django.views.generic import DetailView, ListView, CreateView
from django.shortcuts import get_object_or_404

from .models import Post, Comment, Category

from .forms import CreatePostForm


class PostListView(ListView):
    model = Post
    category = None
    paginate_by = 9

    def get_queryset(self):
        queryset = Post.objects.all()

        category_slug = self.kwargs.get("slug")
        if category_slug:
            self.category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(category=self.category)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.category
        context["categories"] = Category.objects.all()
        return context


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    form_class = CreatePostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentListView(ListView):
    model = Comment
