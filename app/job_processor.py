import json
import os

from job_database import load_jobs, save_jobs


REPORT_FOLDER = "data/reports"



def save_match_report(job):

    os.makedirs(
        REPORT_FOLDER,
        exist_ok=True
    )


    report = {

        "jobId": job["id"],

        "jobTitle": job["title"],

        "company": job["company"],

        "matchScore": job["matchScore"],

        "recommendation": (
            "APPLY"
            if job["matchScore"] >= 80
            else "REVIEW"
        ),

        "summary":
            "Job analyzed successfully.",

        "matchingStrengths": [],

        "skillGaps": [],

        "interviewFocusAreas": []

    }


    report_file = (
        f"{REPORT_FOLDER}/job_{job['id']}_match.json"
    )


    with open(
        report_file,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            report,
            file,
            indent=4
        )


    return report_file



def process_jobs():

    jobs = load_jobs()


    for job in jobs:


        if job["analysisCompleted"]:

            continue



        print("\nProcessing Job")
        print("----------------")

        print(
            job["title"]
        )

        print(
            job["company"]
        )


        print("\nAI Job Analysis...")


        # AI Job Analyzer integration
        # will be connected next



        print("\nAI Match Analysis...")


        # AI Match Agent integration
        # will be connected next



        # Temporary workflow validation

        job["matchScore"] = 90

        job["status"] = "REVIEW"

        job["analysisCompleted"] = True



        report_file = save_match_report(
            job
        )


        job["matchReport"] = report_file



    save_jobs(
        jobs
    )



if __name__ == "__main__":

    process_jobs()

    print(
        "\nJob processing complete."
    )