import json
import re

from app.model.plan import (
    DietPlanResponse
)


class DietPlanResponseParser:

    @staticmethod
    def parse(
            response_text: str
    ) -> DietPlanResponse:

        json_text = (
            DietPlanResponseParser
            ._extract_json(response_text)
        )

        data = json.loads(json_text)

        DietPlanResponseParser._validate(
            data
        )

        return DietPlanResponse(
            breakfast=data["breakfast"],
            lunch=data["lunch"],
            snack=data["snack"],
            dinner=data["dinner"]
        )

    @staticmethod
    def _extract_json(
            response_text: str
    ) -> str:

        # markdown json block

        match = re.search(
            r"```json\s*(.*?)\s*```",
            response_text,
            re.DOTALL
        )

        if match:
            return match.group(1)

        # plain json block

        start = response_text.find("{")
        end = response_text.rfind("}")

        if start == -1 or end == -1:
            raise ValueError(
                "No valid JSON found in OpenAI response."
            )

        return response_text[
            start:end + 1
        ]

    @staticmethod
    def _validate(
            data: dict
    ):

        required_fields = [
            "breakfast",
            "lunch",
            "snack",
            "dinner"
        ]

        for field in required_fields:

            if field not in data:
                raise ValueError(
                    f"Missing field: {field}"
                )

            if not isinstance(
                    data[field],
                    list
            ):
                raise ValueError(
                    f"{field} must be a list"
                )