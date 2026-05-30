from sqlalchemy import func, cast, Date
from app import db
from app.model.food import Food


class FoodRepository:

    def create(self, food: Food):
        db.session.add(food)
        db.session.commit()
        return food

    def find_by_user(self, user_id: int, page: int, page_size: int):
        return (
            Food.query
            .filter(Food.user_id == user_id)
            .order_by(Food.create_time.desc())
            .paginate(page=page, per_page=page_size, error_out=False)
        )

    def summarize_by_date_range(self, user_id: int, start_date, end_date):
        return (
            db.session.query(
                cast(Food.create_time, Date).label("date"),
                func.sum(Food.calories).label("calories"),
                func.sum(Food.carbs).label("carbs"),
                func.sum(Food.protein).label("protein"),
                func.sum(Food.fats).label("fats"),
            )
            .filter(Food.user_id == user_id)
            .filter(cast(Food.create_time, Date) >= start_date)
            .filter(cast(Food.create_time, Date) <= end_date)
            .group_by(cast(Food.create_time, Date))
            .order_by(cast(Food.create_time, Date).asc())
            .all()
        )

    def delete_food_log_by_id(self, user_id, record_id):
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
