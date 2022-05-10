import requests
api_url = "http://127.0.0.1:8000/restpart/car/"
response = requests.get(api_url)
a=response.json()
print(a)
