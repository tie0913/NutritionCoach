import os

from openai import OpenAI


class OpenAIService:

    _client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY")
    )

    _model = os.getenv(
        "OPENAI_MODEL",
        "gpt-4o-mini"
    )

    @staticmethod
    def generate_diet_plan(
            prompt: str
    ) -> str:

        response = OpenAIService._client.responses.create(
            model=OpenAIService._model,
            input=[
                {
                    "role": "system",
                    "content": "You are a professional nutritionist. Return valid JSON only."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
        )

        return response.output_text