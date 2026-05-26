from app import db


class Profile(db.Model):
    __tablename__ = "profiles"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False,
        unique=True
    )

    weight = db.Column(db.Float, nullable=True)
    height = db.Column(db.Float, nullable=True)
    BMR = db.Column(db.Integer, nullable=True)

    chronic = db.Column(db.JSON, nullable=True)
    allergies = db.Column(db.JSON, nullable=True)
    goals = db.Column(db.JSON, nullable=True)

    user = db.relationship(
        "User",
        backref=db.backref("profile", uselist=False)
    )