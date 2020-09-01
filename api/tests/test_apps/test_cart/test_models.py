from tests.factories import CartFactory, ItemFactory


def test_cart_str():
    cart = CartFactory.build()

    assert str(cart) == f"Cart {cart.pk}"


def test_item_str():
    item = ItemFactory.build()

    assert str(item) == f"Item {item.external_id}"
