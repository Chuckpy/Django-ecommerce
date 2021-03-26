import pytest
from django.conf import settings
from django.contrib.sessions.middleware import SessionMiddleware
from django.http import HttpRequest
from products.tests.factories import ProductFactory

from ..cart import Cart

pytestmark = pytest.mark.django_db


def dummy_get_response(request):
    return None


@pytest.fixture
def http_request():
    request = HttpRequest()
    middleware = SessionMiddleware(dummy_get_response)
    middleware.process_request(request)
    return request


@pytest.fixture
def session(http_request):
    return http_request.session


@pytest.fixture
def cart(http_request, session):
    cart = Cart(http_request)
    session.modified = False
    return cart


def test_create_empty_cart(http_request, session):
    assert session.get(settings.CART_SESSION_ID) is None
    Cart(http_request)
    assert session[settings.CART_SESSION_ID] == {}


def test_get_non_empty_cart(http_request, session):
    session[settings.CART_SESSION_ID] = {"1": {}}
    Cart(http_request)
    assert session[settings.CART_SESSION_ID] == {"1": {}}


def test_add_product_to_empty_cart(product, cart, session):
    cart.add(product)

    assert session[settings.CART_SESSION_ID] == {
        str(product.id): {"quantity": 1, "price": str(product.price)}
    }
    assert session.modified


def test_add_product_to_empty_cart_quantity_gt_1(product, cart, session):
    cart.add(product, 2)

    assert session[settings.CART_SESSION_ID] == {
        str(product.id): {"quantity": 2, "price": str(product.price)}
    }
    assert session.modified


def test_add_product_to_empty_cart_twice(product, cart, session):
    cart.add(product)
    session.modified = False

    cart.add(product, 2)

    assert session[settings.CART_SESSION_ID] == {
        str(product.id): {"quantity": 3, "price": str(product.price)}
    }
    assert session.modified


def test_add_product_to_empty_cart_override_quantity(product, cart, session):
    cart.add(product)
    session.modified = False

    cart.add(product, 4, override_quantity=True)

    assert session[settings.CART_SESSION_ID] == {
        str(product.id): {"quantity": 4, "price": str(product.price)}
    }
    assert session.modified


def test_remove_product(product, cart, session):
    cart.add(product)
    session.modified = False

    cart.remove(product)
    assert session[settings.CART_SESSION_ID] == {}
    assert session.modified


def test_remove_product_not_in_cart(product, cart, session):
    cart.remove(product)
    assert session[settings.CART_SESSION_ID] == {}
    assert not session.modified


def test_cart_iter(cart, session):
    p1 = ProductFactory()
    p2 = ProductFactory()
    p3 = ProductFactory()

    cart.add(p1)
    cart.add(p2, 2)
    cart.add(p3, 3)
    session.modified = False

    products = [p1, p2, p3]
    quantities = [1, 2, 3]

    for product, quantity, item in zip(products, quantities, cart):
        assert product.price == item["price"]
        assert product.price * quantity == item["total_price"]
        assert product == item["product"]
        assert "update_quantity_form" in item

    assert not session.modified
    assert list(cart.cart.values()) != list(iter(cart))


def test_cart_length(cart):
    p1 = ProductFactory()
    p2 = ProductFactory()

    assert len(cart) == 0

    cart.add(p1)
    assert len(cart) == 1

    cart.add(p2, 3)
    assert len(cart) == 4


def test_get_total_price(cart):
    p1 = ProductFactory()
    p2 = ProductFactory()

    cart.add(p1)
    cart.add(p2, 2)

    total_price = (p1.price * 1) + (p2.price * 2)

    assert cart.get_total_price() == total_price


def test_cant_add_more_than_max_items(product, cart):
    cart.add(product, settings.CART_ITEM_MAX_QUANTITY)
    assert len(cart) == settings.CART_ITEM_MAX_QUANTITY

    cart.add(product, 1)
    assert len(cart) == settings.CART_ITEM_MAX_QUANTITY