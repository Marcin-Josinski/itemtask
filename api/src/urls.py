from django.urls import path

from src.apps.cart.views import ItemCreateView

urlpatterns = [
    path("item/", ItemCreateView.as_view(), name="item-create"),
]
