import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.3,
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    max_tokens=200
)

def analyze_job(job,skills):
    prompt = f"""
    Analyze this job description and identify the most relevant openings.
    User skills: {skills}

    Job:
    Title: {job['title']}
    Company: {job['company']}
    Location: {job['location']}
    
    Give Only:
    Relevant or Not Relevant
    Score out of 100
    """
    response = llm.invoke(prompt)
    return response.content