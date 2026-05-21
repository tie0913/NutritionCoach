from app import db
from sqlalchemy import func


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    birth_date = db.Column(db.Date, unique=False, nullable=False)
    create_time = db.Column(db.DateTime, unique=False, nullable=False, server_default=func.now())
    update_time = db.Column(db.DateTime, unique=False, nullable=False, server_default=func.now(), onupdate=func.now())

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "birth_date": str(self.birth_date)
        }
