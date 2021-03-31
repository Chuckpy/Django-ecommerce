import factory

from products.tests.factories import ProductFactory

from ..models import Item, Order


class OrderFactory(factory.django.DjangoModelFactory):
    cpf = factory.Faker("cpf", locale="pt_BR")
    name = factory.Faker("name")
    email = factory.Faker("email")
    postal_code = factory.Faker("postcode", locale="pt_BR")
    address = factory.Faker("street_name", locale="pt_BR")
    number = factory.Faker("building_number", locale="pt_BR")
    district = factory.Faker("neighborhood", locale="pt_BR")
    state = factory.Faker("estado_sigla", locale="pt_BR")
    city = factory.Faker("city", locale="pt_BR")

    class Meta:
        model = Order


class ItemFactory(factory.django.DjangoModelFactory):
    order = factory.SubFactory(OrderFactory)
    product = factory.SubFactory(ProductFactory)
    price = factory.Faker("pydecimal", right_digits=2, min_value=5.0, max_value=999.0)
    quantity = factory.Faker("random_int", min=1, max=10)

    class Meta:
        model = Item
