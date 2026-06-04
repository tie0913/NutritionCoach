from datetime import date

from app.model.plan import (
    DietPlanRequest
)


class DietPlanRequestFactory:

    @staticmethod
    def create(
            profile,
            budget: float
    ) -> DietPlanRequest:

        return DietPlanRequest(
            age=DietPlanRequestFactory._calculate_age(
                profile.user.birth_date
            ),
            height=profile.height,
            weight=profile.weight,
            goals=profile.goals,
            chronic=profile.chronic,
            allergies=profile.allergies,
            budget=budget
        )

    @staticmethod
    def _calculate_age(
            birth_date: date
    ) -> int:

        today = date.today()

        age = today.year - birth_date.year

        if (
                today.month,
                today.day
        ) < (
                birth_date.month,
                birth_date.day
        ):
            age -= 1

        return age