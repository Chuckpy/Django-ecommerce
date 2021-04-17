from django.views.generic import DetailView, ListView, CreateView
from django.views import View
from django.shortcuts import redirect, get_object_or_404
from .models import Post, Comment, Category, Favorite

from .forms import CreatePostForm, CreateCommentForm
class PostListView(ListView):
    model = Post
    category = None
    paginate_by = 6

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CreateCommentForm()
        return context
    
    def post(self, request, **kwargs):
        form = CreateCommentForm(request.POST)  
        
        if form.is_valid():
            form.instance.post = self.get_object()
            form.instance.author=request.user
            form.save()
        return redirect(request.path)

class PostCreateView(CreateView):
    model = Post
    form_class = CreatePostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class CommentListView(ListView):
    model = Comment

class FavoriteView(View):

    def post(self,request):

        user = request.user
        post_id = request.POST.get("post_id")
        post_obj = Post.objects.get(id=post_id)
            
        if user in post_obj.favorite.all():
                post_obj.favorite.remove(user)
        else :
                post_obj.favorite.add(user)

        favorite, created = Favorite.objects.get_or_create(author = user, post_id=post_id)

        if not created:
            if favorite.value == "Favoritar":
                favorite.value = "Desfavoritar"
            else:
                favorite.value = "Favoritar"
        favorite.save()

        return redirect(post_obj.get_absolute_url())