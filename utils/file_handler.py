import os
import json

class FileHandler:
    """
    Handles reading and writing files.
    """

    @staticmethod
    def read_json(file_path: str):
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    @staticmethod
    def write_text(file_path: str, content: str):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)

    @staticmethod
    def file_exists(file_path: str):
        return os.path.exists(file_path)