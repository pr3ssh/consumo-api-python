import requests
import json

response = requests.get("http://httpbin.org/get")
if response.status_code == 200:
    print(type(response.text))
    print(response.text)
    # print(type(response.json()))
    # print(response.json())
    dict_data = json.loads(response.text)
    print(type(dict_data))
