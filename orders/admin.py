from django.contrib import admin

from payments.models import Payment

from .models import Item, Order, Review

from products.models import Product


class ItemInline(admin.TabularInline):
    model = Item
    raw_id_fields = ["product"]
    extra = 0


class PaymentInline(admin.TabularInline):
    model = Payment
    can_delete = False
    readonly_fields = (
        "email",
        "doc_number",
        "transaction_amount",
        "installments",
        "payment_method_id",
        "mercado_pago_id",
        "mercado_pago_status",
        "mercado_pago_status_detail",
        "modified",
    )
    ordering = ("-modified",)

    def has_add_permission(self, request, obj):
        return False


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["__str__", "name", "email", "cpf", "paid", "created", "modified"]
    list_filter = ["paid", "created", "modified"]
    search_fields = ["name", "email", "cpf"]
    inlines = [ItemInline, PaymentInline]

    
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["author", "body", "created", "updated","rating"]
    list_filter = ["created","updated"]

    #def formfield_for_foreignkey(self, db_field, request, **kwargs):
     #   if db_field.name == "product":
      #      kwargs["queryset"] = Product.objects.filter(name__in=self.get_form(request).instance.order.items)
       # return super().formfield_for_foreignkey(db_field, request, **kwargs)