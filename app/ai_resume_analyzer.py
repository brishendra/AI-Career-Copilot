from ai_engine import ask_ai
import json
import re


def clean_json_response(response):
    """
    Remove markdown formatting from AI JSON response.
    """

    cleaned = re.sub(
        r"```json|```",
        "",
        response
    )

    return cleaned.strip()


def analyze_resume_with_ai(resume_text):
    """
    Analyze resume using local AI model
    and return structured data.
    """

    prompt = f"""
You are an expert technical recruiter.

Analyze this resume and return ONLY valid JSON.

Do not include explanations.
Do not include markdown formatting.
Return only the JSON object.

Extract these fields:

- yearsOfExperience
- jobRoles
- technicalSkills
- leadershipSkills
- certifications
- majorAchievements

Resume:

{resume_text}
"""

    response = ask_ai(prompt)

    print("\nRAW AI RESPONSE:")
    print(response)

    cleaned_response = clean_json_response(response)

    print("\nCLEANED RESPONSE:")
    print(cleaned_response)

    try:
        profile = json.loads(cleaned_response)

    except json.JSONDecodeError:

        print("\nAI returned invalid JSON.")

        profile = {
            "error": "Invalid AI response",
            "raw_response": response
        }

    return profile


if __name__ == "__main__":

    with open(
        "data/resume_text.txt",
        "r",
        encoding="utf-8"
    ) as file:

        resume_text = file.read()


    resume_profile = analyze_resume_with_ai(
        resume_text
    )


    print("\nAI Resume Profile")
    print("-----------------")

    print(
        json.dumps(
            resume_profile,
            indent=4
        )
    )