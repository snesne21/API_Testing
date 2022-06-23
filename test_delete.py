
import requests
import json
from assertpy.assertpy import assert_that
from config import BASE_URI
import test_post.py


def test_created_item_can_be_deleted():
    item_sku = create_new_sku()

    items = requests.get(BASE_URI).json()
    newly_created_sku = search_created_sku_in(items, item_sku)[0]

    delete_url = f'{BASE_URI}/{newly_created_sku["sku"]}'
    response = requests.delete(delete_url)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)
