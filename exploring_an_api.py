import requests
import json

response = requests.get('https://api.zippopotam.us/de/24848')
print(f'Response status code: {response.status_code}')
print(f'Response headers: {response.headers}')
print(f'Response body: {json.dumps(response.json(), indent=4)}')

data = {
    'place name': 'Amsterdam',
    'country': 'The Netherlands'
}

another_response = requests.post('https://api.zippopotam.us', json=data)
print(f'Response status code: {another_response.status_code}')
print(f'Request payload sent: {another_response.request.body}')