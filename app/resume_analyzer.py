from skills_database import SKILLS


def analyze_resume(text):
    """
    Analyze extracted resume text.
    """

    profile = {
        "certifications": [],
        "skills": [],
        "experience": None
    }

    # Detect certifications
    certifications = [
        "PMP",
        "ITIL",
        "AWS Certified",
        "Azure"
    ]

    for certification in certifications:
        if certification.lower() in text.lower():
            profile["certifications"].append(certification)

    # Detect skills dynamically
    for skill in SKILLS:
        if skill.lower() in text.lower():
            profile["skills"].append(skill)

    # Detect experience
    experience_keywords = [
        "17 years",
        "16 years",
        "15 years",
        "10 years"
    ]

    for experience in experience_keywords:
        if experience in text:
            profile["experience"] = experience
            break

    return profile


if __name__ == "__main__":

    with open("data/resume_text.txt", "r", encoding="utf-8") as file:
        resume_text = file.read()

    resume_profile = analyze_resume(resume_text)

    print("Resume Analysis")
    print("----------------")

    print("\nExperience:")
    print(resume_profile["experience"])

    print("\nCertifications:")
    for cert in resume_profile["certifications"]:
        print("-", cert)

    print("\nSkills:")
    for skill in resume_profile["skills"]:
        print("-", skill)