# AI Career Assistant

An LLM-powered career assistant built with Python and FastAPI. The project provides career guidance, resume-to-role analysis, skill-gap identification, and repeatable LLM evaluation.

## Why I Built This

This project demonstrates practical LLM engineering skills including:

- Prompt engineering
- LLM API integration
- REST API development
- Structured resume analysis
- Skill matching and gap identification
- Test-set based LLM evaluation
- Regression testing for response coverage

## Features

- AI-powered career question answering
- Resume-to-job-role analysis
- Matching skill identification
- Missing skill identification
- Resume improvement suggestions
- Project recommendations
- FastAPI REST endpoints
- Reusable and versioned prompts
- Predefined evaluation test set
- Keyword-based regression evaluation
- Environment-based API key management

## Tech Stack

- Python
- FastAPI
- OpenAI API
- REST APIs
- Prompt Engineering
- Pydantic
- python-dotenv
- JSON
- Uvicorn

## Architecture

```text
User
  |
  v
FastAPI REST API
  |
  +---- /chat ------------> Prompt -> LLM -> Response
  |
  +---- /analyze-resume --> Prompt -> LLM -> Structured Analysis
  |
  +---- /health ----------> Health Check
  |
  v
Evaluation Test Set
  |
  v
Keyword Coverage / Regression Check