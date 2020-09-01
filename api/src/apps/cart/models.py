import uuid

from django.core.validators import MinValueValidator
from django.db import models


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    def __str__(self) -> str:
        return f"Cart {self.id}"


class Item(models.Model):
    external_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    value = models.IntegerField(validators=[MinValueValidator(1)], null=True)
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name="items",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=("external_id", "cart"),
                name="unique_item_in_cart",
            ),
        ]

    def __str__(self) -> str:
        return f"Item {self.external_id}"
