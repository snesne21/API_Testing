import requests

def test_get_request():
  response = requests.get("https://1ryu4whyek.execute-api.us-west-2.amazonaws.com/dev/skus")
  assert (response.status_code == 200), "Status code is not 200 OK. Found this instead:"\
  +str(response.status_code)
  for sku in response.json()['data']:
      if sku['id'] == 'berliner1':
        assert record['price'] == "2.99",\
              "Data does not match! Expected : 2.99, but found : " + str(record['price'])
        assert record['description'] == "Jelly donut",\
              "Data does not match! Expected : Jelly donut, but found : " + str(record['description'])
