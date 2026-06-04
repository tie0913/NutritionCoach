from app.service.ai.request_factory import DietPlanRequestFactory
from app.service.ai.plan_factory import PlanFactory

from app.repository.plan_repo import PlanRepository
from app.repository.profile_repo import ProfileRepository

from app.service.ai.ai_service import OpenAIService
from app.service.ai.response_parser import DietPlanResponseParser
from app.service.ai.prompt_builder import DietPlanPromptBuilder


class PlanService:

    @staticmethod
    def generate_plan(
            user_id: int,
            budget: float
    ):
        profile = ProfileRepository.find_by_user_id(
            user_id
        )

        if profile is None:
            raise ValueError(
                "User profile does not exist."
            )

        diet_plan_request = DietPlanRequestFactory.create(
            profile=profile,
            budget=budget
        )

        prompt = DietPlanPromptBuilder.build(
            diet_plan_request
        )

        openai_response = OpenAIService.generate_diet_plan(
            prompt
        )

        diet_plan_response = DietPlanResponseParser.parse(
            openai_response
        )

        plan = PlanFactory.create(
            user_id=user_id,
            response=diet_plan_response
        )

        return PlanRepository.save(
            plan
        )

    @staticmethod
    def list_plan(
            user_id: int,
            page: int,
            page_size: int
    ):
        return PlanRepository.find_by_user_id(
            user_id=user_id,
            page=page,
            page_size=page_size
        )