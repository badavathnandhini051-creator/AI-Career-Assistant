# AI Career Assistant

An LLM-powered AI Career Assistant built with Python and FastAPI to provide career guidance, resume analysis, skill-gap identification, and role-specific recommendations.

## Features

- AI-powered career guidance using an LLM
- Resume analysis for a target job role
- Matching skills and missing skills identification
- Project and resume improvement suggestions
- Prompt engineering with structured system prompts
- REST API development using FastAPI
- LLM evaluation using a predefined test set
- Keyword-based evaluation for response coverage
- Secure API key management using environment variables

## Tech Stack

- Python
- FastAPI
- OpenAI API
- Prompt Engineering
- REST APIs
- Pydantic
- python-dotenv
- JSON-based test cases
- Uvicorn

## Project Architecture

```text
User
  |
  v
FastAPI
  |
  +---- /chat ------------> LLM
  |
  +---- /analyze-resume --> LLM
  |
  +---- /health ----------> Health Check
  |
  v
JSON Response