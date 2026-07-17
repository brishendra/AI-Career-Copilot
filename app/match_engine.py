def calculate_match(resume_profile, job_profile):
    """
    Compare resume skills with job requirements.
    """

    resume_skills = set(resume_profile["skills"])
    job_skills = set(job_profile["skills"])

    matched_skills = resume_skills.intersection(job_skills)
    missing_skills = job_skills.difference(resume_skills)

    if len(job_skills) > 0:
        match_percentage = (
            len(matched_skills) / len(job_skills)
        ) * 100
    else:
        match_percentage = 0

    result = {
        "match_percentage": round(match_percentage, 2),
        "matched_skills": list(matched_skills),
        "missing_skills": list(missing_skills)
    }

    return result


if __name__ == "__main__":

    resume_profile = {
        "skills": [
            "Project Management",
            "Cloud",
            "Infrastructure",
            "Agile",
            "AWS"
        ]
    }

    job_profile = {
        "skills": [
            "Project Management",
            "Cloud",
            "Infrastructure",
            "Agile",
            "AWS",
            "Azure"
        ]
    }

    match_result = calculate_match(
        resume_profile,
        job_profile
    )

    print("Job Match Analysis")
    print("------------------")

    print(
        "Match Score:",
        match_result["match_percentage"],
        "%"
    )

    print("\nMatched Skills:")
    for skill in match_result["matched_skills"]:
        print("-", skill)

    print("\nMissing Skills:")
    for skill in match_result["missing_skills"]:
        print("-", skill)