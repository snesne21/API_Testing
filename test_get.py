
import requests
from assertpy.assertpy import assert_that
from config import BASE_URI

def test_get_request():
  response = requests.get(BASE_URI)
  assert_that(response.status_code).is_equal_to(requests.codes.ok)
  response_text = response.json()
  skus = [item['sku'] for item in response_text]
  assert_that(skus).contains('berliner2')

  for item in response.json():
      if item['sku'] == 'berliner1':
        assert item['price'] == "2.99",\
              "Data does not match! Expected : 2.99, but found : " + str(item['price'])
        assert item['description'] == "Jelly donut",\
              "Data does not match! Expected : Jelly donut, but found : " + str(item['description'])
  
