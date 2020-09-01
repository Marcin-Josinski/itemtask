import pytest
from rest_framework import status
from rest_framework.reverse import reverse

from src.apps.cart.models import Item, Cart
from src.settings import SESSION_COOKIE_KEY
from tests.factories import CartFactory, ItemFactory


@pytest.mark.django_db
def test_create_item_when_session_exists(api_client, item_data):
    # GIVEN
    cart = CartFactory.create()
    api_client.cookies[SESSION_COOKIE_KEY] = cart.pk

    # WHEN
    response = api_client.post(reverse("item-create"), data=item_data)

    # THEN
    assert Item.objects.filter(external_id=item_data["external_id"]).exists()
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_create_item_when_session_not_exists(api_client, item_data):
    # WHEN
    response = api_client.post(reverse("item-create"), data=item_data)

    # THEN
    assert Cart.objects.exists()

    cart = Cart.objects.first()
    assert response.cookies[SESSION_COOKIE_KEY].value == str(cart.pk)
    assert Item.objects.filter(cart=cart).exists()
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_update_existing_item(api_client, item_data):
    # GIVEN
    cart = CartFactory.create()
    item = ItemFactory.create(cart=cart)
    api_client.cookies[SESSION_COOKIE_KEY] = cart.pk

    # WHEN
    response = api_client.post(
        reverse("item-create"),
        data={
            "external_id": item.external_id,
            "name": item_data["name"],
        },
    )

    # THEN
    assert Item.objects.get(external_id=item.external_id).name == item_data["name"]
    assert response.status_code == status.HTTP_204_NO_CONTENT
