import pytest
import requests

API_URL = 'http://127.0.0.1:8000'
AUTH_TOKEN = 'ceb232845ecb1d9423ba385ea49952af4260a588'

def test_list_students():
    response = requests.get(f'{API_URL}/', headers={'Authorization': f'Token {AUTH_TOKEN}'})
    assert response.status_code == 200

if __name__ == '__main__':
    pytest.main()
