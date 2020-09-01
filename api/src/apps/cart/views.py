from django.db import transaction
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from src.apps.cart.models import Cart, Item
from src.apps.cart.serializers import ItemCreateInputSerializer
from src.apps.cart.services import set_session


class ItemCreateView(APIView):
    def post(self, request: Request) -> Response:
        serializer = ItemCreateInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        response = Response(status=status.HTTP_204_NO_CONTENT)
        try:
            cart_id = request.COOKIES["cart_id"]
        except KeyError:
            with transaction.atomic():
                cart = Cart.objects.create()
                Item.objects.create(cart=cart, **serializer.validated_data)
            set_session(response=response, cart=cart)
        else:
            Item.objects.update_or_create(
                cart=get_object_or_404(Cart, pk=cart_id),
                external_id=serializer.validated_data.pop("external_id"),
                defaults={**serializer.validated_data},
            )

        return response
