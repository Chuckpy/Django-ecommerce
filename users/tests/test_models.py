import pytest

from ..models import User

pytestmark = pytest.mark.django_db


def test_create_user():
    user = User.objects.create_user(
        username="usuario_test", email="usuario@test.com", password="passw0rd"
    )

    assert user.username == "usuario_test"
    assert user.email == "usuario@test.com"
    assert user.is_active
    assert not user.is_staff
    assert not user.is_superuser


def test_create_superuser():
    user = User.objects.create_superuser(
        username="admin_test", email="admin@test.com", password="passw0rd"
    )
    assert user.username == "admin_test"
    assert user.email == "admin@test.com"
    assert user.is_active
    assert user.is_staff
    assert user.is_superuser