import os

from dotenv import load_dotenv
from google import genai

from prompts import RESUME_ANALYSIS_PROMPT

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def analyze_resume(resume_text):
    prompt = RESUME_ANALYSIS_PROMPT.format(resume_text)

    models = [
        "gemini-flash-latest",
        "gemini-2.0-flash",
        "gemini-3.1-flash-lite",
    ]

    for model in models:
        try:
            response = client.models.generate_content(
                model=model,
                contents=prompt
            )
            return response.text
        except Exception:
            continue

    return "Unable to contact Gemini. Please try again in a few minutes."