import json
from datetime import datetime

from job_database import load_jobs, save_jobs



def normalize_job(job):

    return {
        "id": None,
        "title": job.get("title", ""),
        "company": job.get("company", ""),
        "location": job.get("location", ""),
        "source": job.get("source", ""),
        "url": job.get("url", ""),
        "description": job.get("description", ""),
        "dateFound": datetime.now().isoformat(),
        "status": "NEW",
        "matchScore": None,
        "analysisCompleted": False
    }



def job_exists(jobs, new_job):

    for job in jobs:

        if (
            job["title"].lower()
            == new_job["title"].lower()
            and
            job["company"].lower()
            == new_job["company"].lower()
        ):
            return True

    return False



def add_job(job):

    jobs = load_jobs()


    normalized_job = normalize_job(job)


    if job_exists(
        jobs,
        normalized_job
    ):

        print("Job already exists.")

        return



    normalized_job["id"] = (
        len(jobs) + 1
    )


    jobs.append(
        normalized_job
    )


    save_jobs(
        jobs
    )


    print(
        "Job added successfully."
    )



if __name__ == "__main__":


    sample_job = {

        "title": "Cloud Program Manager",

        "company": "Amazon",

        "location": "Remote",

        "source": "Company Career Page",

        "url": "https://amazon.jobs/sample",

        "description":
            "Lead cloud transformation programs "
            "across enterprise infrastructure teams."

    }


    add_job(
        sample_job
    )