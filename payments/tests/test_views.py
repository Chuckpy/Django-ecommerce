import json

import pytest
from django.urls import resolve, reverse
from pytest_django.asserts import assertTemplateUsed

from orders.tests.factories import ProductFactory

from .factories import PaymentFactory, PaymentFormFactory

pytestmark = pytest.mark.django_db


@pytest.fixture
def client_with_order(client, order_form_data):
    p = ProductFactory(price=1.0)
    client.post(
        reverse("cart:add", kwargs={"product_id": p.id}),
        data={"quantity": 1, "override": False},
    )
    client.post(reverse("orders:create"), order_form_data, follow=True)
    return client


def test_reverse_resolve():
    assert reverse("payments:process") == "/payments/process/"
    assert resolve("/payments/process/").view_name == "payments:process"

    assert reverse("payments:failure") == "/payments/failure/"
    assert resolve("/payments/failure/").view_name == "payments:failure"

    assert reverse("payments:pending") == "/payments/pending/"
    assert resolve("/payments/pending/").view_name == "payments:pending"

    assert reverse("payments:success") == "/payments/success/"
    assert resolve("/payments/success/").view_name == "payments:success"

    assert reverse("payments:webhook") == "/payments/webhook/"
    assert resolve("/payments/webhook/").view_name == "payments:webhook"


def test_status_code(client):
    response = client.get(reverse("payments:process"))
    assert response.status_code == 404

    response = client.get(reverse("payments:failure"))
    assert response.status_code == 200

    response = client.get(reverse("payments:pending"))
    assert response.status_code == 200

    response = client.get(reverse("payments:success"))
    assert response.status_code == 200

    response = client.get(reverse("payments:webhook"))
    assert response.status_code == 405


def test_payment_success(client_with_order, mocker):
    mocker.patch(
        "mercadopago.resources.Payment.create",
        return_value={
            "status": 201,
            "response": {
                "id": "123",
                "status_detail": "accredited",
                "status": "approved",
            },
        },
    )
    payment_data = PaymentFormFactory(transaction_amount=1.0)
    response = client_with_order.post(
        reverse("payments:process"), payment_data, follow=True
    )
    assertTemplateUsed(response, "payments/success.html")


def test_payment_failure(client_with_order, mocker):
    mocker.patch(
        "mercadopago.resources.Payment.create",
        return_value={
            "status": 201,
            "response": {
                "id": "123",
                "status_detail": "cc_rejected_bad_filled_card_number",
                "status": "rejected",
            },
        },
    )
    payment_data = PaymentFormFactory(transaction_amount=1.0)
    response = client_with_order.post(
        reverse("payments:process"), payment_data, follow=True
    )
    assertTemplateUsed(response, "payments/failure.html")


def test_payment_pending(client_with_order, mocker):
    mocker.patch(
        "mercadopago.resources.Payment.create",
        return_value={
            "status": 201,
            "response": {
                "id": "123",
                "status_detail": "pending_review_manual",
                "status": "in_process",
            },
        },
    )
    payment_data = PaymentFormFactory(transaction_amount=1.0)
    response = client_with_order.post(
        reverse("payments:process"), payment_data, follow=True
    )
    assertTemplateUsed(response, "payments/pending.html")


def test_payment_webhook(order, client, product, mocker):
    PaymentFactory(order=order, mercado_pago_id="12345")
    mocker.patch(
        "mercadopago.resources.Payment.get",
        return_value={
            "response": {
                "status": "approved",
                "status_detail": "accredited",
            },
        },
    )
    payment_data = {
        "action": "payment.updated",
        "data": {
            "id": "12345",
        },
    }
    response = client.post(
        reverse("payments:webhook"),
        json.dumps(payment_data),
        content_type="application/json",
    )
    assert response.status_code == 200
