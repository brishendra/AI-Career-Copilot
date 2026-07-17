import json
from datetime import datetime



JOBS_FILE = "data/jobs.json"



def load_jobs():

    with open(
        JOBS_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)



def print_header():

    print()
    print("=" * 50)
    print("        AI CAREER COPILOT DASHBOARD")
    print("=" * 50)
    print()



def display_summary(jobs):

    total = len(jobs)

    analyzed = len(
        [
            job
            for job in jobs
            if job.get("analysisCompleted")
        ]
    )


    apply_jobs = len(
        [
            job
            for job in jobs
            if job.get("status") == "APPLY"
        ]
    )


    review_jobs = len(
        [
            job
            for job in jobs
            if job.get("status") == "REVIEW"
        ]
    )


    print("SUMMARY")
    print("-" * 50)

    print(f"Total Jobs: {total}")
    print(f"Analyzed: {analyzed}")
    print(f"Ready to Apply: {apply_jobs}")
    print(f"Need Review: {review_jobs}")

    print()



def display_jobs(jobs):

    print("JOB PIPELINE")
    print("-" * 50)


    for job in jobs:


        print(
            f"""
Title:
{job.get("title")}

Company:
{job.get("company")}

Location:
{job.get("location")}

Status:
{job.get("status")}

Match Score:
{job.get("matchScore")}

Source:
{job.get("source")}

URL:
{job.get("url")}

{"-" * 50}
"""
        )



def run_dashboard():

    jobs = load_jobs()


    print_header()


    print(
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )

    print()


    display_summary(
        jobs
    )


    display_jobs(
        jobs
    )



if __name__ == "__main__":

    run_dashboard()