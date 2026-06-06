from sqlalchemy import func, cast, Date
from app import db
from app.model.food import Food


class FoodRepository:

    @staticmethod
    def create(food: Food):
        db.session.add(food)
        db.session.commit()
        return food

    @staticmethod
    def find_by_user(user_id: int, page: int, page_size: int):
        return (
            Food.query
            .filter(Food.user_id == user_id)
            .order_by(Food.create_time.desc())
            .paginate(page=page, per_page=page_size, error_out=False)
        )

    @staticmethod
    def summarize_by_date_range(user_id: int, start_date, end_date):
        return (
            Food.query
            .filter(Food.user_id == user_id)
            .filter(Food.create_time >= start_date)
            .filter(Food.create_time < end_date)
            .all()
        )


    @staticmethod
    def delete_food_log_by_id(user_id, record_id):
        food_log = Food.query.filter(
            Food.id == record_id,
            Food.user_id == user_id
        ).first()
        if not food_log:
            return False
        else:
            db.session.delete(food_log)
            db.session.commit()
            return True
