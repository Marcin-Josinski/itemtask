from rest_framework.response import Response

from src.apps.cart.models import Cart
from src.settings import SESSION_COOKIE_KEY, SESSION_COOKIE_AGE


def set_session(*, response: Response, cart: Cart) -> None:
    response.set_cookie(
        key=SESSION_COOKIE_KEY,
        value=str(cart.pk),
        max_age=SESSION_COOKIE_AGE,
    )
