import pytest

from .factories import PaymentFactory

pytestmark = pytest.mark.django_db


def test___str__(order):
    payment = PaymentFactory(order=order)
    assert payment.__str__() == f"Pagamento {payment.id}"
    assert str(payment) == f"Pagamento {payment.id}"
