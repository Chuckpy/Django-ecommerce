from django.contrib import admin

from .models import Item, Order


class ItemInline(admin.TabularInline):
    model = Item
    raw_id_fields = ["product"]
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["__str__", "name", "email", "cpf", "paid", "created", "modified"]
    list_filter = ["paid", "created", "modified"]
    search_fields = ["name", "email", "cpf"]
    inlines = [ItemInline]