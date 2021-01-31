from fastapi.testclient import TestClient

from ..app import app


URI = '/'


def test_hello():
    with TestClient(app) as client:
        response = client.get(URI)
        response_dict = response.json()
        assert response.status_code == 200
        assert 'message' in response_dict
