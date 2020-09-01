import factory.fuzzy

from src.apps.cart.models import Item, Cart


class CartFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Cart


class ItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Item

    external_id = factory.Faker("uuid4")
    name = factory.Faker("word")
    value = factory.Faker("pyint", min_value=1)
    cart = factory.SubFactory(CartFactory)
