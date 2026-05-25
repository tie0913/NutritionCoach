from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # register blueprint
    from app.api.user_api import user_bp
    app.register_blueprint(user_bp)


    app.config["JWT_SECRET_KEY"] = Config.SECRET_KEY
    jwt = JWTManager(app)

    return app