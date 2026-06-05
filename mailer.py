import smtplib
import os
from email.mime.text import MIMEText

from dotenv import load_dotenv

load_dotenv()

def send_email(jobs):
    sender = os.getenv("EMAIL_SENDER")
    password = os.getenv("EMAIL_PASSWORD")
    receiver = os.getenv("EMAIL_RECEIVER")

    body = " Top matching jobs for you:\n\n"

    for job in jobs:
        body += f"""
Title: {job['title']}
Company: {job['company']}
Location: {job['location']}
Link: {job['link']}

--------------
"""
        
    msg = MIMEText(body)
    msg['Subject'] = "Your Job Matches"
    msg['From'] = sender
    msg['To'] = receiver

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, receiver, msg.as_string())
    server.quit()