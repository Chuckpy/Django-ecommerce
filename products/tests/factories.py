import factory
import factory.fuzzy

from ..models import Category, Product


class CategoryFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText()

    class Meta:
        model = Category


class ProductFactory(factory.django.DjangoModelFactory):
    category = factory.SubFactory(CategoryFactory)
    name = factory.fuzzy.FuzzyText()
    image = factory.django.ImageField()
    description = factory.Faker("paragraph", nb_sentences=3, variable_nb_sentences=True)
    price = factory.fuzzy.FuzzyDecimal(5.0, 999.99)
    is_available = factory.Faker("pybool")

    class Meta:
        model = Product