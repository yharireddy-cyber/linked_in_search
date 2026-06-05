import schedule
import time

from scraper import scrape_linkedin_jobs
from database import create_table, insert_job
from agent import analyze_job
from mailer import send_email

SKILLS = """
AZURE
KUBERNETES
LangChain
Python
Machine Learning
Generative AI
Docker
"""

def run_agent():
    print("Running AI Job Search Agent...")
    jobs = scrape_linkedin_jobs("AI Engineer")

    relevant_jobs = []
    for job in jobs:
        result = analyze_job(job, SKILLS)
        job['score'] = result
        if "Relevant" in result:
            relevant_jobs.append(job)
            insert_job(job)

    if relevant_jobs:
        send_email(relevant_jobs)
        print("Email sent with relevant jobs!")
    else:
        print("No relevant jobs found.")

schedule.every(6).hours.do(run_agent)

while True:
    schedule.run_pending()
    time.sleep(60)
