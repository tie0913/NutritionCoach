from app.model.plan import (
    DietPlanResponse, Plan
)

class PlanFactory:

    @staticmethod
    def create(
            user_id: int,
            response: DietPlanResponse
    ) -> Plan:

        return Plan(
            user_id=user_id,

            breakfast=response.breakfast,

            lunch=response.lunch,

            snack=response.snack,

            dinner=response.dinner
        )