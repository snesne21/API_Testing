import requests
from uuid import uuid4
import json
import random
from assertpy.assertpy import assert_that
from config import BASE_URI

def test_new_sku_can_be_added():
    unique_sku = create_new_sku()

    # After sku is created, we read all the skus and then use list comprehension to find if the
    # created sku is present in the response list
    items = requests.get(BASE_URI).json()
    is_new_sku_created = search_created_sku_in(items, unique_sku)
    assert_that(is_new_sku_created).is_not_empty()

def create_new_sku():
    # Ensure a sku with a unique sku text is created everytime the test runs
    # json.dumps() -convert python dict to json string

    unique_sku = f'sku {str(uuid4())}'
    payload = json.dumps({
        'description': unique_sku,
        'sku': unique_sku,
        'price': random.uniform(2.0, 10.5)
    })

    # Setting default headers to show that the client accepts json
    # And will send json in the headers
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    # We use requests.post method with keyword params to make the request more readable
    response = requests.post(url=BASE_URI, data=payload, headers=headers)
    assert_that(response.status_code, description='SKU created successfully').is_equal_to(requests.codes.ok)
    return unique_sku

def search_created_sku_in(items, unique_sku):
    return [item for item in items if item['sku'] == unique_sku]
