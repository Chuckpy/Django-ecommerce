from django.contrib import admin

from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "order",
        "doc_number",
        "email",
        "transaction_amount",
        "mercado_pago_id",
        "mercado_pago_status",
        "mercado_pago_status_detail",
        "created",
        "modified",
    ]
    list_filter = ["mercado_pago_status", "modified"]
    search_fields = ["doc_number", "email", "mercado_pago_id"]