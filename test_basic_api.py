import requests

query = """
query getRocketData($id: ID!)
{
  rocket(id: $id) {
    name
    country
  }
}
"""

payload = {
    'query': query,
    'variables': {
        'id': 'falcon1'
    }
}

def test_graphql():
    response = requests.post('https://api.spacex.land/graphql/', json=payload)
    assert response.status_code == 200
    body = response.json()
    assert body['data']['rocket']['name'] == 'Falcon 1'
    assert body['data']['rocket']['country'] == 'Republic of the Marshall Islands'
