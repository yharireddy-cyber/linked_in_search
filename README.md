# LinkedIn Search

A Python Streamlit app for scraping LinkedIn jobs, scoring them with Google Gemini via LangChain, storing results in SQLite, and sending matching jobs by email.

## Features

- Search LinkedIn jobs by keyword and optional location
- Scrape job title, company, location, and job link
- Score relevance with a Google Generative AI model
- Save results to a local SQLite database (`jobs.db`)
- Send selected relevant jobs by email
- Run locally or inside Docker

## Repository Structure

- `app.py` - Streamlit UI and orchestration
- `scraper.py` - LinkedIn job scraping logic using Playwright
- `agent.py` - LLM scoring with LangChain and Gemini
- `database.py` - SQLite persistence functions
- `mailer.py` - SMTP email sender
- `Dockerfile` - container build definition
- `requirements.txt` - Python package dependencies
- `.env` - local environment variables (not checked in)

## Requirements

- Python 3.11+
- Docker (optional, for containerized deployment)

## Environment Variables

Create a `.env` file in the project root with:

```env
GOOGLE_API_KEY=<your-google-api-key>
EMAIL_SENDER=<your-email-address>
EMAIL_PASSWORD=<your-email-password-or-app-password>
EMAIL_RECEIVER=<target-email-address>
```

> For Gmail SMTP, use an app password if two-factor authentication is enabled.

## Local Setup

1. Create and activate a virtual environment:

```powershell
cd D:\ai-training\linked_in_search
python -m venv venv
.\venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
python -m playwright install --with-deps
```

3. Run the app:

```powershell
streamlit run app.py
```

4. Open the local Streamlit UI:

```text
http://localhost:8501
```

## Docker Setup

Build the Docker image:

```powershell
docker build -t linkedin .
```

Run the container:

```powershell
docker run -itd -p 8602:8501 --env-file .env --name linkedinsearch linkedin
```

Access the app at:

```text
http://localhost:8602
```

## Usage

- Enter your skills and job keyword
- Optionally provide a location (city/state/country)
- Click `Find Jobs`
- The app scrapes jobs, scores relevance, and stores matching jobs
- Click `Send Email with Relevant Jobs` to email results

## Notes

- The scraper uses LinkedIn page selectors; if LinkedIn changes their layout, selectors may need updating.
- The email sender currently uses Gmail SMTP; ensure the sender account is configured to allow SMTP access.
- If you hit quota limits for the Gemini model, upgrade your Google API plan or reduce request volume.
