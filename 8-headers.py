import requests
import json



def pprint(content):
    print(json.dumps(content, indent=4))



url = 'https://api.punkapi.com/v2/beers'
params = {
        'abv_gt': 6,
        'beer_name': 'IPA',
        'page': 1,
        'per_page': 1
        }

response = requests.get(url, params=params)
if response.ok:
    pprint(dict(response.headers))
    pprint(response.json())
