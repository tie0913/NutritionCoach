from app.model.food import Food
from app.api.schema.food_schema import FoodResponseSchema
from app.repository.food_repo import FoodRepository


class FoodService:

    @staticmethod
    def create_food(user_id: int, data: dict):
        food = Food(
            user_id=user_id,
            name=data["name"],
            quantity=data["quantity"],
            calories=data["calories"],
            carbs=data["carbs"],
            protein=data["protein"],
            fats=data["fats"],
        )

        saved_food = FoodRepository.create(food)
        return FoodResponseSchema().dump(saved_food)

    @staticmethod
    def list_foods(user_id: int, page: int, page_size: int):
        pagination = FoodRepository.find_by_user(user_id, page, page_size)

        return {
            "items": FoodResponseSchema(many=True).dump(pagination.items),
            "page": pagination.page,
            "page_size": pagination.per_page,
            "total": pagination.total,
            "pages": pagination.pages,
        }

    @staticmethod
    def get_diagram_data(user_id: int, start_date, end_date):
        return FoodRepository.summarize_by_date_range(
            user_id=user_id,
            start_date=start_date,
            end_date=end_date
        )

    @staticmethod
    def delete_food_log_by_id(user_id, record_id):
        return FoodRepository.delete_food_log_by_id(user_id, record_id)
