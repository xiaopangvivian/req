import requests

response = requests.get("https://g1api.finlogixtesting.com/v1/post/all")

print(response.status_code)

print(response.text)

print(response.content)

print(response.json())