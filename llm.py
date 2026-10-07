import os
from dotenv import load_dotenv
from openai import OpenAI

from prompts.prompts import CAREER_ASSISTANT_PROMPT, RESUME_ANALYSIS_PROMPT

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL = os.getenv("OPENAI_MODEL")


def generate_response(message: str) -> str:
    prompt = f"{CAREER_ASSISTANT_PROMPT}\n\nUser: {message}"

    response = client.responses.create(
        model=MODEL,
        input=prompt
    )

    return response.output_text


def analyze_resume(resume_text: str, target_role: str) -> str:
    prompt = RESUME_ANALYSIS_PROMPT.format(
        resume_text=resume_text,
        target_role=target_role
    )

    response = client.responses.create(
        model=MODEL,
        input=prompt
    )

    return response.output_text