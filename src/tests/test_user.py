def test_registration(client):
    response = client.post('/register', data={
        'username': 'testuser2',
        'password': 'testpass2'
    })
    assert response.status_code == 302 #checking proper redirection
    assert response.location.endswith('/login') #checking where we end up

def test_user_login(client):
    client.post('/register', data={
        'username': 'testuser2',
        'password': 'testpass2'
    })
    response = client.post('/login', data={
        'username': 'testuser2',
        'password': 'testpass2'
    })
    assert response.status_code == 200 #successful login
