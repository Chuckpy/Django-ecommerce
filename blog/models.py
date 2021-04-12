from users.models import User
from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel


from .utils import upload_perfil_user


class Category(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="name")

    class Meta:
        ordering = ("name",)
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("blog:list_by_category", kwargs={"slug": self.slug})


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="title")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=1050)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True, upload_to=upload_perfil_user)
    favorite = models.IntegerField(null=True, default=0)
    category = models.ForeignKey(
        Category, related_name="posts", on_delete=models.CASCADE, null=True
    )
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
