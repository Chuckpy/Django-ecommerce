from django.db import models
from localflavor.br.models import BRCPFField
from model_utils.models import TimeStampedModel

from orders.models import Order


class Payment(TimeStampedModel):
    order = models.ForeignKey(Order, related_name="payments", on_delete=models.CASCADE)
    transaction_amount = models.DecimalField(
        "Valor da Transação", max_digits=10, decimal_places=2
    )
    installments = models.IntegerField("Parcelas")
    payment_method_id = models.CharField("Método de Pagamento", max_length=250)
    email = models.EmailField()
    doc_number = BRCPFField("CPF")
    mercado_pago_id = models.CharField(max_length=250, blank=True, db_index=True)
    mercado_pago_status = models.CharField(max_length=250, blank=True)
    mercado_pago_status_detail = models.CharField(max_length=250, blank=True)

    class Meta:
        ordering = ("-modified",)

    def __str__(self):
        return f"Pagamento {self.id}"