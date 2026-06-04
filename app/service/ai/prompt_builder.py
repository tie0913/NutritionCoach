from app.model.plan import (
    DietPlanRequest
)


class DietPlanPromptBuilder:

    @staticmethod
    def build(
            request: DietPlanRequest
    ) -> str:

        return f"""
You are a professional nutritionist.

Create a healthy one-day diet plan.

User Information

Age:
{request.age}

Height:
{request.height} cm

Weight:
{request.weight} kg

Goals:
{DietPlanPromptBuilder._format_list(request.goals)}

Chronic Diseases:
{DietPlanPromptBuilder._format_list(request.chronic)}

Allergies:
{DietPlanPromptBuilder._format_list(request.allergies)}

Budget Per Meal:
{request.budget} CAD

Requirements

1. The meal plan must support the user's goals.
2. Avoid all allergic foods.
3. Consider all chronic diseases.
4. Keep each meal within the budget.
5. Use common foods available in Canada.
6. Provide breakfast, lunch, snack and dinner.
7. Return JSON only.
8. Do not return markdown.
9. Do not explain anything.

Response Format

{{
    "breakfast": [
        "food item"
    ],
    "lunch": [
        "food item"
    ],
    "snack": [
        "food item"
    ],
    "dinner": [
        "food item"
    ]
}}
""".strip()

    @staticmethod
    def _format_list(items) -> str:

        if not items:
            return "None"

        return ", ".join(items)