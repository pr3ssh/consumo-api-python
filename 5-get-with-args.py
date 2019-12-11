import requests
import json


city_name = "Milwaukee"
location_query = "https://www.metaweather.com/api/location/search/?query={}"
# location_query = "https://www.metaweather.com/api/location/search/"
weather_query = "https://www.metaweather.com/api/location/{}/"

response = requests.get(location_query.format(city_name))
# response = requests.get(location_query, params={'query': city_name})
if response.ok:
    response = requests.get(weather_query.format(response.json()[0]['woeid']))
    if response.ok:
        print(json.dumps(response.json(), ensure_ascii=True, indent=4
                ))
