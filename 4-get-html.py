import requests

response = requests.get("http://mit.edu")
if response.status_code == 200:
    print(response.text)
