from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from flask import Flask, request, g
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

    @app.before_request
    def load_timezone():

        timezone = request.headers.get(
            "Timezone",
            "UTC"
        )

        try:
            ZoneInfo(timezone)
            g.timezone = timezone

        except ZoneInfoNotFoundError:
            g.timezone = "UTC"

    # register blueprint
    from app.api.user_api import user_bp
    from app.api.profile_api import profile_bp
    from app.api.food_api import food_bp
    from app.api.plan_api import plan_bp

    app.register_blueprint(user_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(food_bp)
    app.register_blueprint(plan_bp)


    app.config["JWT_SECRET_KEY"] = Config.SECRET_KEY
    jwt = JWTManager(app)

    return app