from ai_engine import ask_ai
import json
import re


def clean_json_response(response):
    """
    Extract JSON object from AI response.
    """

    match = re.search(
        r"\{.*\}",
        response,
        re.DOTALL
    )

    if match:
        return match.group(0).strip()

    return response.strip()



def load_json_file(file_path):
    """
    Load JSON data from file.
    """

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)



def validate_match_report(report):
    """
    Ensure AI response contains useful fields.
    """

    if not report.get("summary"):

        report["summary"] = (
            f"{report.get('jobTitle', 'This role')} "
            "is a strong potential opportunity based on "
            "the candidate's experience, skills, and certifications."
        )


    if not report.get("matchingStrengths"):

        report["matchingStrengths"] = [
            "Relevant professional experience identified"
        ]


    if not report.get("skillGaps"):

        report["skillGaps"] = [
            "No significant skill gaps identified"
        ]


    if not report.get("resumeImprovements"):

        report["resumeImprovements"] = [
            "No major resume changes required"
        ]


    if not report.get("interviewFocusAreas"):

        report["interviewFocusAreas"] = [
            "Discuss relevant project experience and leadership examples"
        ]


    return report



def analyze_match_with_ai(resume_profile, job_profile):
    """
    Compare candidate profile with job profile.
    """

    prompt = f"""
You are a senior technical recruiter and career advisor.

Evaluate this candidate against this job opportunity.

Return ONLY JSON.
Do not include markdown.
Do not include explanations before or after JSON.

Rules:

matchScore must be a percentage between 0 and 100.

Scoring:

90-100:
Excellent match.

75-89:
Strong match. Candidate should apply.

60-74:
Moderate match.

Below 60:
Weak match.

Recommendation must be:
APPLY
or
SKIP


Return this exact JSON structure:

{{
    "jobTitle": "",
    "matchScore": 0,
    "recommendation": "",
    "summary": "",
    "matchingStrengths": [],
    "skillGaps": [],
    "resumeImprovements": [],
    "interviewFocusAreas": []
}}


Candidate Profile:

{json.dumps(resume_profile, indent=2)}


Job Profile:

{json.dumps(job_profile, indent=2)}

"""


    response = ask_ai(prompt)


    print("\nRAW AI RESPONSE:")
    print(response)


    cleaned_response = clean_json_response(
        response
    )


    print("\nCLEANED RESPONSE:")
    print(cleaned_response)


    try:

        report = json.loads(
            cleaned_response
        )


    except json.JSONDecodeError:

        report = {
            "error": "Invalid AI response",
            "raw_response": response
        }


    if "error" not in report:

        report = validate_match_report(
            report
        )


    return report



def save_report(report, output_file):
    """
    Save match report.
    """

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            report,
            file,
            indent=4
        )



if __name__ == "__main__":

    resume_profile = load_json_file(
        "data/resume_profile.json"
    )


    job_profile = load_json_file(
        "data/job_profile.json"
    )


    match_report = analyze_match_with_ai(
        resume_profile,
        job_profile
    )


    save_report(
        match_report,
        "data/match_report.json"
    )


    print("\nAI Career Recommendation")
    print("-----------------------")


    print(
        json.dumps(
            match_report,
            indent=4
        )
    )


    print(
        "\nSaved to: data/match_report.json"
    )