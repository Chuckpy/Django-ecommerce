import json

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.utils.functional import cached_property
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.generic import CreateView, TemplateView

from orders.models import Order

from .forms import PaymentForm, UpdatePaymentForm
from .models import Payment


class PaymentCreateView(CreateView):
    model = Payment
    form_class = PaymentForm

    @cached_property
    def order(self):
        order_id = self.request.session.get("order_id")
        order = get_object_or_404(Order, id=order_id)
        return order

    def get_form_kwargs(self):
        form_kwargs = super().get_form_kwargs()
        form_kwargs["order"] = self.order
        return form_kwargs

    def form_valid(self, form):
        form.save()
        redirect_url = "payments:failure"
        status = form.instance.mercado_pago_status

        if status == "approved":
            redirect_url = "payments:success"
        if status == "in_process":
            redirect_url = "payments:pending"

        if status and status != "rejected":
            del self.request.session["order_id"]
        return redirect(redirect_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["order"] = self.order
        context["publishable_key"] = settings.MERCADO_PAGO_PUBLIC_KEY
        return context


class PaymentFailureView(TemplateView):
    template_name = "payments/failure.html"


class PaymentPendingView(TemplateView):
    template_name = "payments/pending.html"


class PaymentSuccessView(TemplateView):
    template_name = "payments/success.html"


@csrf_exempt
@require_POST
def payment_webhook(request):
    data = json.loads(request.body)
    form = UpdatePaymentForm(data)
    if form.is_valid():
        form.save()

    return JsonResponse({})