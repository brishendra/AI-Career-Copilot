from ai_engine import ask_ai
import json
import re


def clean_json_response(response):
    """
    Remove markdown formatting from AI response.
    """

    cleaned = re.sub(
        r"```json|```",
        "",
        response
    )

    return cleaned.strip()


def analyze_job_with_ai(job_text):
    """
    Analyze a job description using the local AI model.
    """

    prompt = f"""
You are an expert technical recruiter.

Analyze the following job description.

Return ONLY valid JSON.
Do not include markdown.
Do not include explanations.

Extract:

- jobTitle
- company
- location
- remoteStatus
- requiredExperience
- requiredSkills
- preferredSkills
- certifications
- responsibilities
- atsKeywords

Job Description:

{job_text}
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


def save_profile(profile, output_file):
    """
    Save the AI-generated job profile as JSON.
    """

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            profile,
            file,
            indent=4
        )


if __name__ == "__main__":

    with open(
        "documents/job_descriptions/sample_job.txt",
        "r",
        encoding="utf-8"
    ) as file:

        job_text = file.read()

    job_profile = analyze_job_with_ai(job_text)

    save_profile(
        job_profile,
        "data/job_profile.json"
    )

    print("\nAI Job Profile")
    print("----------------")

    print(
        json.dumps(
            job_profile,
            indent=4
        )
    )

    print("\nJob profile saved to: data/job_profile.json")