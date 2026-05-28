from datetime import datetime
from app import db

class Food(db.Model):
    __tablename__ = "food_logs"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False,
        index=True
    )

    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Float, nullable=False)

    calories = db.Column(db.Integer, nullable=False)
    carbs = db.Column(db.Integer, nullable=False)
    protein = db.Column(db.Integer, nullable=False)
    fats = db.Column(db.Integer, nullable=False)

    create_time = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow,
        index=True
    )