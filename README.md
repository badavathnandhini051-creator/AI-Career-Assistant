# AI Career Assistant

An LLM-powered career assistant built with Python, FastAPI, REST APIs, prompt engineering, and LLM evaluation.

## Why I built this

This project demonstrates practical LLM engineering skills: prompt design, API integration, structured resume analysis, REST endpoints, and repeatable evaluation test cases.

## Features

- Career question answering using an LLM
- Resume-to-job-role analysis
- Matching and missing skill identification
- Project and resume improvement suggestions
- FastAPI REST endpoints
- Versioned prompt templates
- Evaluation test set with keyword-based regression checks
- Environment-variable based API key management

## Architecture

```text
User
  |
  v
FastAPI REST API
  |
  +---- /chat ------------> Prompt -> LLM -> Response
  |
  +---- /analyze-resume --> Prompt -> LLM -> JSON -> Response
  |
  v
Evaluation Test Set
  |
  v
Keyword Coverage / Regression Check
```

## Tech Stack

- Python
- FastAPI
- OpenAI Responses API
- REST API
- Prompt Engineering
- JSON
- LLM Evaluation

## Project Structure

```text
AI-Career-Assistant/
├── app.py
├── llm.py
├── evaluate.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── prompts/
│   ├── __init__.py
│   └── prompts.py
└── tests/
    └── test_cases.json
```

## Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd AI-Career-Assistant
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Configure the API key

Create a `.env` file in the project root:

```text
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-6-luna
```

Never upload `.env` to GitHub.

### 5. Start the API

```powershell
uvicorn app:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

FastAPI will show an interactive Swagger UI where you can test the endpoints.

## API Endpoints

### GET /health

Checks whether the API is running.

### POST /chat

Example request:

```json
{
  "message": "What skills should I learn for a Python developer internship?"
}
```

### POST /analyze-resume

Example request:

```json
{
  "resume_text": "Python, SQL, pandas, machine learning...",
  "target_role": "AI/ML Intern"
}
```

## LLM Evaluation

The `tests/test_cases.json` file contains representative prompts and expected concepts. `evaluate.py` runs every test case and reports keyword coverage.

This is intentionally a lightweight evaluation layer for a portfolio project. In a production system, evaluation would also include semantic similarity, factuality, safety, latency, failure rates, and human review.

Run:

```powershell
python evaluate.py
```

## Prompt Engineering

The project keeps prompts in `prompts/prompts.py` instead of mixing them throughout the application code. This makes prompts easier to review, update, and version.

## Security Notes

- API keys are stored in environment variables.
- `.env` is excluded through `.gitignore`.
- User input is length-limited by the API schema.
- The assistant is instructed not to invent candidate experience.

## Future Improvements

- Add conversation history
- Add function/tool calling for external career APIs
- Add semantic evaluation with an LLM judge
- Add a web interface
- Add automated CI tests
- Add conversation analytics and drop-off metrics
- Deploy the API to a cloud platform

## Resume Project Description

**AI Career Assistant | Python, FastAPI, LLM API, Prompt Engineering, REST API**
- Built an LLM-powered career assistant with FastAPI REST endpoints for career Q&A and resume-to-role analysis.
- Designed reusable prompts and structured JSON outputs for skill matching, skill-gap analysis, and resume recommendations.
- Created an evaluation test set and regression runner to measure response quality using repeatable keyword-coverage checks.
