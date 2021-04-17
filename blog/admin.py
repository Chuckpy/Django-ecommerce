from django.contrib import admin

from .models import Post, Comment, Category, Favorite

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "created", "updated", )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "created", "updated", "post")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "created", "modified"]

@admin.register(Favorite)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "post", "value","created", "updated")