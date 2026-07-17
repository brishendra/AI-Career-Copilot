import json
import os
from datetime import datetime


DATABASE_FILE = "data/jobs.json"


def initialize_database():
    """
    Create the jobs database if it does not exist.
    """

    if not os.path.exists(DATABASE_FILE):

        with open(
            DATABASE_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                [],
                file,
                indent=4
            )


def load_jobs():
    """
    Load all jobs from the database.
    """

    initialize_database()

    with open(
        DATABASE_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def save_jobs(jobs):
    """
    Save all jobs to the database.
    """

    with open(
        DATABASE_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            jobs,
            file,
            indent=4
        )


def job_exists(jobs, url):
    """
    Check whether a job already exists.
    """

    for job in jobs:

        if job["url"] == url:
            return True

    return False


def add_job(
    title,
    company,
    location,
    source,
    url,
    description
):
    """
    Add a new job to the database.
    """

    jobs = load_jobs()

    if job_exists(jobs, url):

        print("Job already exists.")

        return


    job = {

        "id": len(jobs) + 1,

        "title": title,

        "company": company,

        "location": location,

        "source": source,

        "url": url,

        "description": description,

        "dateFound": datetime.now().isoformat(),

        "status": "NEW",

        "matchScore": None,

        "analysisCompleted": False
    }

    jobs.append(job)

    save_jobs(jobs)

    print("Job added successfully.")


def get_all_jobs():
    """
    Return all stored jobs.
    """

    return load_jobs()


if __name__ == "__main__":

    initialize_database()

    add_job(
        title="Senior IT Program Manager",
        company="Microsoft",
        location="Remote",
        source="LinkedIn",
        url="https://linkedin.com/job/sample123",
        description="Cloud transformation leadership role."
    )

    jobs = get_all_jobs()

    print("\nStored Jobs")
    print("-----------")

    for job in jobs:

        print(f"ID: {job['id']}")
        print(f"Title: {job['title']}")
        print(f"Company: {job['company']}")
        print(f"Location: {job['location']}")
        print(f"Status: {job['status']}")
        print(f"Match Score: {job['matchScore']}")
        print("-" * 40)