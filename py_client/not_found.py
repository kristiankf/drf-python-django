import requests

endpoint = "http://127.0.0.1:8000/api/products/3000/"

get_response = requests.get(endpoint, json={"title": "Hello world"})
print(get_response.json())
