import sys
from pathlib import Path

from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from app import app  # noqa: E402

client = TestClient(app)


def test_health():
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json() == {'status': 'ok'}


def test_blank_activity_rejected():
    response = client.post('/api/entries', json={'goal': '   ', 'minutes': 10})
    assert response.status_code == 422


def test_invalid_minutes_rejected():
    response = client.post('/api/entries', json={'goal': 'study', 'minutes': 1441})
    assert response.status_code == 422
