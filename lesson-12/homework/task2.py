import requests
import sqlite3
import csv
from bs4 import BeautifulSoup

# Define the website URL
URL = "https://realpython.github.io/fake-jobs"
DB_NAME = "jobs.db"


# Function to create the database and table if not exists
def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_title TEXT NOT NULL,
            company TEXT NOT NULL,
            location TEXT NOT NULL,
            description TEXT NOT NULL,
            application_link TEXT NOT NULL,
            UNIQUE(job_title, company, location)
        )
    """)

    conn.commit()
    conn.close()


# Function to scrape job listings
def scrape_jobs():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []

    # Find all job postings
    job_cards = soup.find_all("div", class_="card-content")

    for job in job_cards:
        job_title = job.find("h2", class_="title").text.strip()
        company = job.find("h3", class_="company").text.strip()
        location = job.find("p", class_="location").text.strip()
        description_tag = job.find("div", class_="description")
        description = description_tag.text.strip() if description_tag else "No description available"

        application_tag = job.find("a", string="Apply")
        application_link = application_tag.get("href") if application_tag else "No link available"

        jobs.append((job_title, company, location, description, application_link))

    return jobs


# Function to insert or update jobs in the database
def store_jobs(jobs):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    for job in jobs:
        job_title, company, location, description, application_link = job

        cursor.execute("""
            SELECT description, application_link FROM jobs 
            WHERE job_title = ? AND company = ? AND location = ?
        """, (job_title, company, location))

        existing_job = cursor.fetchone()

        if existing_job:
            # Check if description or link has changed
            if existing_job[0] != description or existing_job[1] != application_link:
                cursor.execute("""
                    UPDATE jobs
                    SET description = ?, application_link = ?
                    WHERE job_title = ? AND company = ? AND location = ?
                """, (description, application_link, job_title, company, location))
        else:
            cursor.execute("""
                INSERT INTO jobs (job_title, company, location, description, application_link)
                VALUES (?, ?, ?, ?, ?)
            """, (job_title, company, location, description, application_link))

    conn.commit()
    conn.close()


# Function to filter jobs by location or company
def filter_jobs(location=None, company=None):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    query = "SELECT * FROM jobs WHERE 1=1"
    params = []

    if location:
        query += " AND location LIKE ?"
        params.append(f"%{location}%")
    if company:
        query += " AND company LIKE ?"
        params.append(f"%{company}%")

    cursor.execute(query, params)
    results = cursor.fetchall()

    conn.close()
    return results


# Function to export jobs to CSV
def export_to_csv(filtered_jobs, filename="filtered_jobs.csv"):
    headers = ["ID", "Job Title", "Company", "Location", "Description", "Application Link"]

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(filtered_jobs)

    print(f"Filtered job listings exported to {filename}")


# Main execution
if __name__ == "__main__":
    create_database()

    print("Scraping job listings...")
    jobs = scrape_jobs()

    print("Storing jobs in the database...")
    store_jobs(jobs)

    print("Done! Jobs are updated in the database.")

    # Example: Filtering jobs
    print("\nFiltered jobs (Location: Remote):")
    filtered_jobs = filter_jobs(location="Remote")
    for job in filtered_jobs:
        print(job)

    # Export filtered jobs to CSV
    export_to_csv(filtered_jobs)
