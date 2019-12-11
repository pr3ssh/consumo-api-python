import requests


response = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Jimmy_Wales_Fundraiser_Appeal.JPG/797px-Jimmy_Wales_Fundraiser_Appeal.JPG', stream=True)

with open('img.jpg', 'wb') as image:
    for chunk in response.iter_content():
        image.write(chunk)

response.close()

