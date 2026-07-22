import re

class Helpers:
    """
    Utility helper functions.
    """

    @staticmethod
    def clean_filename(name: str):

        name = name.strip()

        name = re.sub(r'[\\/*?:"<>|]', "", name)

        return name.replace(" ", "_")

    @staticmethod
    def capitalize_words(text: str):

        return text.title()

    @staticmethod
    def format_phone(phone: str):

        return phone.strip()

    @staticmethod
    def format_email(email: str):

        return email.strip().lower()