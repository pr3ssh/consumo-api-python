import requests
import json


url = 'http://httpbin.org/post'
payload = {'a': 1}

response = requests.post(url, data=json.dumps(payload))
# response = requests.post(url, json=payload)
if response.ok:
    print(response.text)
