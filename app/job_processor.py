import json

from job_database import load_jobs, save_jobs


JOBS_PROFILE_FILE = "data/job_profile.json"
MATCH_REPORT_FILE = "data/match_report.json"


def process_jobs():

    jobs = load_jobs()

    for job in jobs:

        if job["analysisCompleted"]:
            continue


        print("\nProcessing Job")
        print("----------------")
        print(job["title"])
        print(job["company"])


        print("\nAI Job Analysis...")

        # AI Job Analyzer integration will be connected here


        print("\nAI Match Analysis...")

        # AI Match Agent integration will be connected here


        # Temporary workflow validation

        job["matchScore"] = 90

        job["status"] = "REVIEW"

        job["analysisCompleted"] = True


    save_jobs(jobs)


if __name__ == "__main__":

    process_jobs()

    print("\nJob processing complete.")