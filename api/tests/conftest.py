import pytest
from rest_framework.test import APIClient

from tests.factories import ItemFactory


@pytest.fixture()
def api_client():
    return APIClient()


@pytest.fixture()
def item_data():
    item = ItemFactory.build()

    return {
        "external_id": item.external_id,
        "name": item.name,
        "value": item.value,
    }
