import pytest
from django.contrib.admin.sites import AdminSite

from payments.models import Payment

from ..admin import PaymentInline

pytestmark = pytest.mark.django_db


def test_has_add_permission(request):
    assert (
        PaymentInline(Payment, AdminSite()).has_add_permission(request, None) is False
    )
