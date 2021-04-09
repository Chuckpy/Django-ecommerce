from django.contrib import admin

from .models import Post, Comment, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "created", "updated", "favorite")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "created", "updated", "post")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "created", "modified"]
