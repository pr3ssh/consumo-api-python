import requests
import json


api_url = 'https://api.github.com/user'
gh_url = 'https://github.com/pr3ssh-test'

session = requests.session()
session.auth = ('', '')
response = session.get(api_url)
if response.ok:
    response = session.get(gh_url)
    if response.ok:
        print(response.cookies)
