from app import db


class Plan(db.Model):

    __tablename__ = "plan"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    breakfast = db.Column(
        db.JSON,
        nullable=False
    )

    lunch = db.Column(
        db.JSON,
        nullable=False
    )

    snack = db.Column(
        db.JSON,
        nullable=False
    )

    dinner = db.Column(
        db.JSON,
        nullable=False
    )

    create_time = db.Column(
        db.DateTime,
        nullable=False,
        server_default=db.func.current_timestamp()
    )

from dataclasses import dataclass
from typing import List

@dataclass
class DietPlanRequest:
    age: int
    height: float
    weight: float
    goals: List[str]
    chronic: List[str]
    allergies: List[str]
    budget: float


@dataclass
class DietPlanResponse:
    breakfast: List[str]
    lunch: List[str]
    snack: List[str]
    dinner: List[str]