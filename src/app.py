from flask import Flask
from config import Config
from models import db
from controllers.user_controller import users_bp
from services.auth_service import jwt

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)

    # Register blueprints
    app.register_blueprint(users_bp)

   # Create database schema only if not testing
    with app.app_context():
        if not app.config.get('TESTING', False):
            db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5555)
