from rest_framework.response import Response

from src.apps.cart.services import set_session
from src.settings import SESSION_COOKIE_KEY, SESSION_COOKIE_AGE
from tests.factories import CartFactory


def test_set_session():
    # GIVEN
    response = Response()
    cart = CartFactory.build()

    # WHEN
    set_session(response=response, cart=cart)

    # THEN
    cookie = response.cookies[SESSION_COOKIE_KEY]
    assert cookie.value == str(cart.pk)
    assert cookie["max-age"] == SESSION_COOKIE_AGE
