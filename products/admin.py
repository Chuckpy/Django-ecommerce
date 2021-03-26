from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "created", "modified"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "slug",
        "category",
        "price",
        "is_available",
        "created",
        "modified",
    ]
    list_filter = ["is_available", "created", "modified"]
    list_editable = ["price", "is_available"]