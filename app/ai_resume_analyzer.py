from ai_engine import ask_ai
import json


def analyze_resume_with_ai(resume_text):
    """
    Analyze resume using local AI model.
    """

    prompt = f"""
You are an expert technical recruiter.

Analyze this resume and extract:

1. Years of experience
2. Job roles
3. Technical skills
4. Leadership skills
5. Certifications
6. Major achievements

Return ONLY valid JSON.

Resume:

{resume_text}
"""

    response = ask_ai(prompt)

    return response


if __name__ == "__main__":

    with open(
        "data/resume_text.txt",
        "r",
        encoding="utf-8"
    ) as file:
        resume_text = file.read()


    result = analyze_resume_with_ai(
        resume_text
    )

    print(result)