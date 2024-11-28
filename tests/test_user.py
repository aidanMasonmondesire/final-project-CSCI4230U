def test_registration(client):
    response = client.post('/register', json={
        'username': 'testuser',
        'password': 'testpass'
    })
    assert response.status_code == 201
    assert response.get_json()['message'] == 'User registered successfully'

def test_user_login(client):
    client.post('/register', json={
        'username': 'testuser',
        'password': 'testpass'
    })
    response = client.post('/login', json={
        'username': 'testuser',
        'password': 'testpass'
    })
    assert response.status_code == 200
    assert 'access_token' in response.get_json()



