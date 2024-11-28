def test_registration(client):
    response = client.post('/register', json={
        'username': 'testuser',
        'password': 'testpass'
    })
    assert response.status_code == 302
    assert response.location.endswith('/login')

def test_user_login(client):
    client.post('/register', json={
        'username': 'testuser',
        'password': 'testpass'
    })
    response = client.post('/login', json={
        'username': 'testuser',
        'password': 'testpass'
    })
    assert response.status_code == 302
    assert response.location.endswith('/home') 



