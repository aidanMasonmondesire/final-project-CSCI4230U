import pytest
import sys
import os

# Add the project root directory to sys.path so that we can take stuff from models and app
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models import db
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True #testing purposes
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['JWT_SECRET_KEY'] = 'test_jwt_secret_key'

    with app.test_client() as client:
        with app.app_context():
            yield client

        # Cleanup after tests
    with app.app_context():
        db.session.remove()
        db.drop_all()