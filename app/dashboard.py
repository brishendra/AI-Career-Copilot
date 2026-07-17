import json
from datetime import datetime


JOBS_FILE = "data/jobs.json"



def load_json(file_path):

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)



def print_header():

    print()
    print("=" * 60)
    print("             AI CAREER COPILOT DASHBOARD")
    print("=" * 60)
    print()



def load_match_report(job):

    report_file = job.get(
        "matchReport"
    )


    if not report_file:

        return {}


    try:

        return load_json(
            report_file
        )


    except FileNotFoundError:

        return {}



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
    print("-" * 60)

    print(f"Total Jobs       : {total}")
    print(f"Analyzed Jobs    : {analyzed}")
    print(f"Ready To Apply   : {apply_jobs}")
    print(f"Needs Review     : {review_jobs}")

    print()



def display_match_details(report):

    if not report:

        print(
            "AI Recommendation: Not available"
        )

        return



    print("AI RECOMMENDATION")
    print("-" * 60)


    print(
        f"Recommendation : {report.get('recommendation')}"
    )


    print(
        f"Match Score    : {report.get('matchScore')}%"
    )


    print()


    print("Summary:")

    print(
        report.get(
            "summary",
            "Not available"
        )
    )


    print()


    print("Matching Strengths:")


    for item in report.get(
        "matchingStrengths",
        []
    ):

        print(
            f"  ✓ {item}"
        )


    print()


    print("Skill Gaps:")


    for item in report.get(
        "skillGaps",
        []
    ):

        print(
            f"  ⚠ {item}"
        )


    print()


    print("Interview Focus Areas:")


    for item in report.get(
        "interviewFocusAreas",
        []
    ):

        print(
            f"  • {item}"
        )


    print()



def display_jobs(jobs):

    print("JOB PIPELINE")
    print("-" * 60)


    for job in jobs:


        print()


        print(
            job.get("title")
        )


        print(
            f"Company : {job.get('company')}"
        )


        print(
            f"Status  : {job.get('status')}"
        )


        print(
            f"Score   : {job.get('matchScore')}%"
        )


        print(
            f"Source  : {job.get('source')}"
        )


        print()


        report = load_match_report(
            job
        )


        display_match_details(
            report
        )


        print(
            "-" * 60
        )



def run_dashboard():

    jobs = load_json(
        JOBS_FILE
    )


    print_header()


    print(
        "Generated:",
        datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
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