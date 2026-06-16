import requests

response = requests.post(
    "http://localhost:8080/batch/run"
)

print(response.text)