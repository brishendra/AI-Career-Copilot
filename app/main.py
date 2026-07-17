from resume_parser import extract_resume_text, save_extracted_text
from resume_analyzer import analyze_resume
from job_analyzer import analyze_job_description
from match_engine import calculate_match


def main():

    print("==============================")
    print("AI Career Copilot")
    print("==============================")

    # Step 1: Extract resume text
    resume_path = "documents/resume/sample_resume.pdf"
    resume_output = "data/resume_text.txt"

    print("\nReading resume...")

    resume_text = extract_resume_text(resume_path)

    save_extracted_text(
        resume_text,
        resume_output
    )

    print("Resume extracted successfully")


    # Step 2: Analyze resume
    print("\nAnalyzing resume...")

    resume_profile = analyze_resume(
        resume_text
    )


    # Step 3: Analyze job description
    print("\nAnalyzing job description...")

    job_path = "documents/job_descriptions/sample_job.txt"

    with open(
        job_path,
        "r",
        encoding="utf-8"
    ) as file:
        job_text = file.read()


    job_profile = analyze_job_description(
        job_text
    )


    # Step 4: Match resume and job
    print("\nCalculating job match...")

    match_result = calculate_match(
        resume_profile,
        job_profile
    )


    # Step 5: Display report

    print("\n==============================")
    print("Career Copilot Report")
    print("==============================")

    print(
        "\nMatch Score:",
        match_result["match_percentage"],
        "%"
    )


    print("\nMatched Skills:")

    for skill in match_result["matched_skills"]:
        print("-", skill)


    print("\nMissing Skills:")

    for skill in match_result["missing_skills"]:
        print("-", skill)



if __name__ == "__main__":
    main()