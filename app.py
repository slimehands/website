from flask import Flask
from config import Config
from extensions import bcrypt, login_manager
from routes import register_routes
from models import User
from typing import Optional

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # Configure Flask-Login
    #login_view: Optional[str] = 'auth.login_route'
    login_manager.login_view = 'auth.login_route'
    login_manager.login_message_category = 'info'

    @login_manager.user_loader
    def load_user(user_id):
        # Modify this to use raw SQL
        return User.get(user_id)

    # Register routes
    register_routes(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=8000)
