import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# -----------------------------
# Application Information
# -----------------------------

APP_NAME = "SmartResume AI"
APP_VERSION = "1.0.0"

# -----------------------------
# OpenAI Configuration
# -----------------------------

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

MODEL_NAME = "gpt-4.1-mini"

MAX_TOKENS = 1500

TEMPERATURE = 0.7

# -----------------------------
# Export Paths
# -----------------------------

PDF_EXPORT_FOLDER = "exports/pdf"

DOCX_EXPORT_FOLDER = "exports/docx"

# -----------------------------
# Supported File Types
# -----------------------------

SUPPORTED_EXPORTS = [
    "pdf",
    "docx"
]

# -----------------------------
# Resume Sections
# -----------------------------

RESUME_SECTIONS = [
    "Personal Information",
    "Career Objective",
    "Education",
    "Skills",
    "Experience",
    "Projects",
    "Certifications",
    "Languages"
]