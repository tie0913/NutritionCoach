from app.model.food import Food
from app.api.schema.food_schema import FoodResponseSchema
from app.repository.food_repo import FoodRepository


class FoodService:

    def __init__(self, food_repo:FoodRepository):
        self.food_repo = food_repo

    def create_food(self, user_id: int, data: dict):
        food = Food(
            user_id=user_id,
            name=data["name"],
            quantity=data["quantity"],
            calories=data["calories"],
            carbs=data["carbs"],
            protein=data["protein"],
            fats=data["fats"],
        )

        saved_food = self.food_repo.create(food)
        return FoodResponseSchema().dump(saved_food)

    def list_foods(self, user_id: int, page: int, page_size: int):
        pagination = self.food_repo.find_by_user(user_id, page, page_size)

        return {
            "items": FoodResponseSchema(many=True).dump(pagination.items),
            "page": pagination.page,
            "page_size": pagination.per_page,
            "total": pagination.total,
            "pages": pagination.pages,
        }

    def get_diagram_data(self, user_id: int, start_date, end_date):
        rows = self.food_repo.summarize_by_date_range(
            user_id=user_id,
            start_date=start_date,
            end_date=end_date
        )

        return [
            {
                "date": row.date.isoformat(),
                "calories": int(row.calories or 0),
                "carbs": int(row.carbs or 0),
                "protein": int(row.protein or 0),
                "fats": int(row.fats or 0),
            }
            for row in rows
        ]

    def delete_food_log_by_id(self, user_id, record_id):
        return self.food_repo.delete_food_log_by_id(user_id, record_id)
