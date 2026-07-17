def analyze_resume(text):
    """
    Analyze extracted resume text.
    """

    profile = {
        "certifications": [],
        "skills": [],
        "experience": None
    }

    # Certification detection
    if "PMP" in text:
        profile["certifications"].append("PMP")

    if "ITIL" in text:
        profile["certifications"].append("ITIL")

    # Skill detection
    skills_list = [
        "Program Management",
        "Cloud",
        "Infrastructure",
        "Agile",
        "Stakeholder Management"
    ]

    for skill in skills_list:
        if skill.lower() in text.lower():
            profile["skills"].append(skill)

    # Experience detection
    if "17 years" in text:
        profile["experience"] = "17 years"

    return profile


if __name__ == "__main__":

    with open("data/resume_text.txt", "r", encoding="utf-8") as file:
        resume_text = file.read()

    resume_profile = analyze_resume(resume_text)

    print("Resume Analysis")
    print("----------------")

    print("Experience:")
    print(resume_profile["experience"])

    print("\nCertifications:")
    for cert in resume_profile["certifications"]:
        print("-", cert)

    print("\nSkills:")
    for skill in resume_profile["skills"]:
        print("-", skill)