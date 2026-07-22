import os

from openai import OpenAI

from config.settings import MODEL_NAME
from config.prompts import SYSTEM_PROMPT

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


class ResumeGenerator:
    """
    Generates AI-powered resumes.
    """

    @staticmethod
    def generate(prompt: str) -> str:

        response = client.responses.create(
            model=MODEL_NAME,
            input=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.output_text