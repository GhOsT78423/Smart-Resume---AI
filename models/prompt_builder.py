from config.prompts import RESUME_PROMPT


class PromptBuilder:
    """
    Builds prompts for AI resume generation.
    """

    @staticmethod
    def build_resume_prompt(data: dict) -> str:
        return RESUME_PROMPT.format(
            name=data.get("name", ""),
            email=data.get("email", ""),
            phone=data.get("phone", ""),
            education=data.get("education", ""),
            skills=data.get("skills", ""),
            experience=data.get("experience", ""),
            projects=data.get("projects", ""),
            certifications=data.get("certifications", ""),
            languages=data.get("languages", ""),
            objective=data.get("objective", "")
        )