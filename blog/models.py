from users.models import User
from django.db import models
from django.urls import reverse


def upload_perfil_user(instance, filename):
    return f"profile_pictures/user_{instance.id}/{filename}"
class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=1050)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True, upload_to=upload_perfil_user)
    favorite = models.IntegerField(null=True, default=0)
    
    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})

    def comment_number(self):
        return len(self.comment_set.all())

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    