import requests

endpoint = "http://127.0.0.1:8000/api/products/"

get_response = requests.post(endpoint, json={"title": "Go go ga go ga gogo"})
print(get_response.json())
