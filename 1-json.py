import requests
import json

# print(json.dumps(
#     {
#         'a':2,
#         'b': {
#             'x':3,
#             'y': {
#                 't1': 4,
#                 't2': 5
#                 }
#             }
#     }, sort_keys=True, indent=4))


# Add load, loads, dump
# print(json.loads('{"a": 12}'))
#
# print(json.dumps(json.loads(requests.get('https://data.what-politicians-say.poletika.org/json/').text), indent=4))

print(json.load(open('1-json.json', 'r')))
