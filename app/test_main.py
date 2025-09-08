import pytest
from app.main import app
import json

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_endpoint(client):
    response = client.get('/')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'healthy'

def test_get_items_empty(client):
    response = client.get('/api/items')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['count'] == 0

def test_create_item(client):
    response = client.post('/api/items', 
                         json={'name': 'Test Item', 'description': 'A test item'})
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['name'] == 'Test Item'
    assert 'id' in data

def test_get_item(client):
    create_response = client.post('/api/items', 
                                json={'name': 'Test Item', 'description': 'A test item'})
    item_id = json.loads(create_response.data)['id']
    response = client.get(f'/api/items/{item_id}')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['name'] == 'Test Item'

def test_update_item(client):
    create_response = client.post('/api/items', 
                                json={'name': 'Test Item', 'description': 'A test item'})
    item_id = json.loads(create_response.data)['id']
    response = client.put(f'/api/items/{item_id}', 
                         json={'name': 'Updated Item'})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['name'] == 'Updated Item'

def test_delete_item(client):
    create_response = client.post('/api/items', 
                                json={'name': 'Test Item', 'description': 'A test item'})
    item_id = json.loads(create_response.data)['id']
    response = client.delete(f'/api/items/{item_id}')
    assert response.status_code == 200
    response = client.get(f'/api/items/{item_id}')
    assert response.status_code == 404
