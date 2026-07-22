"""
Prompt templates used by SmartResume AI.
"""

SYSTEM_PROMPT = """
You are an expert Resume Writer and Career Coach.

Your responsibility is to create professional ATS-friendly resumes.

Rules:

1. Use formal English.
2. Keep the resume concise.
3. Highlight strengths.
4. Use bullet points wherever appropriate.
5. Do not invent information.
6. Improve grammar.
7. Make the resume suitable for recruiters.
8. Return only the resume.
"""

RESUME_PROMPT = """
Create a professional ATS-friendly resume using the information below.

Name:
{name}

Email:
{email}

Phone:
{phone}

Education:
{education}

Skills:
{skills}

Experience:
{experience}

Projects:
{projects}

Certifications:
{certifications}

Languages:
{languages}

Career Objective:
{objective}

Formatting Requirements:

- Professional Heading
- Career Objective
- Education
- Technical Skills
- Work Experience
- Projects
- Certifications
- Languages

Use concise bullet points and professional formatting.
"""