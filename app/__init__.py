from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    # register blueprint
    from app.api.user_api import user_bp
    app.register_blueprint(user_bp)

    return app