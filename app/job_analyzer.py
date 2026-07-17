from skills_database import SKILLS


def analyze_job_description(text):
    """
    Analyze a job description and extract requirements.
    """

    job_profile = {
        "skills": [],
        "certifications": [],
        "experience": None
    }

    # Detect skills
    for skill in SKILLS:
        if skill.lower() in text.lower():
            job_profile["skills"].append(skill)

    # Detect certifications
    certifications = [
        "PMP",
        "ITIL",
        "AWS Certified",
        "Azure"
    ]

    for certification in certifications:
        if certification.lower() in text.lower():
            job_profile["certifications"].append(certification)

    # Detect experience requirements
    experience_keywords = [
        "10+ years",
        "8+ years",
        "5+ years",
        "3+ years"
    ]

    for experience in experience_keywords:
        if experience in text:
            job_profile["experience"] = experience
            break

    return job_profile


if __name__ == "__main__":

    with open(
        "documents/job_descriptions/sample_job.txt",
        "r",
        encoding="utf-8"
    ) as file:
        job_text = file.read()

    job_profile = analyze_job_description(job_text)

    print("Job Analysis")
    print("----------------")

    print("\nExperience:")
    print(job_profile["experience"])

    print("\nCertifications:")
    for cert in job_profile["certifications"]:
        print("-", cert)

    print("\nSkills:")
    for skill in job_profile["skills"]:
        print("-", skill)