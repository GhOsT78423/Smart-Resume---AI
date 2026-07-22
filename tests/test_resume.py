import unittest

from models.validator import Validator
from models.prompt_builder import PromptBuilder

class TestResumeProject(unittest.TestCase):

    def test_valid_email(self):
        self.assertTrue(
            Validator.validate_email("john@example.com")
        )

    def test_invalid_email(self):
        self.assertFalse(
            Validator.validate_email("johnexample.com")
        )

    def test_valid_phone(self):
        self.assertTrue(
            Validator.validate_phone("+919876543210")
        )

    def test_invalid_phone(self):
        self.assertFalse(
            Validator.validate_phone("12345")
        )

    def test_required_fields(self):

        data = {
            "name": "John Doe",
            "email": "john@example.com",
            "phone": "+919876543210",
            "education": "B.E Computer Science",
            "skills": "Python, Java"
        }

        missing = Validator.validate_required_fields(data)

        self.assertEqual(missing, [])

    def test_prompt_generation(self):

        data = {
            "name": "John Doe",
            "email": "john@example.com",
            "phone": "+919876543210",
            "education": "B.E Computer Science",
            "skills": "Python",
            "experience": "Intern",
            "projects": "SmartResume AI",
            "certifications": "Python",
            "languages": "English",
            "objective": "Software Engineer"
        }

        prompt = PromptBuilder.build_resume_prompt(data)

        self.assertIn("John Doe", prompt)
        self.assertIn("Python", prompt)
        self.assertIn("Software Engineer", prompt)

if __name__ == "__main__":
    unittest.main()