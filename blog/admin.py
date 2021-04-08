from django.contrib import admin

from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "created", "updated", "favorite")
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = ( "author", "created", "updated","post")
