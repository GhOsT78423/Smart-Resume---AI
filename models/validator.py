import re

class Validator:
    """
    Validates resume input fields.
    """

    @staticmethod
    def validate_email(email: str) -> bool:
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return bool(re.match(pattern, email))

    @staticmethod
    def validate_phone(phone: str) -> bool:
        pattern = r"^\+?[0-9]{10,15}$"
        return bool(re.match(pattern, phone))

    @staticmethod
    def validate_required_fields(data: dict):

        required = [
            "name",
            "email",
            "phone",
            "education",
            "skills"
        ]

        missing = []

        for field in required:
            value = data.get(field)

            if value is None or str(value).strip() == "":
                missing.append(field)

        return missing