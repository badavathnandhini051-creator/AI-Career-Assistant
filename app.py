import json

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from llm import generate_response, analyze_resume

app = FastAPI(title="AI Career Assistant", version="1.0.0")

class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=4000)

class ResumeRequest(BaseModel):
    resume_text: str = Field(min_length=20, max_length=12000)
    target_role: str = Field(min_length=2, max_length=200)

@app.get("/")
def root():
    return {"message": "AI Career Assistant API is running", "docs": "/docs"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/chat")
def chat(request: ChatRequest):
    try:
        answer = generate_response(request.message)
        return {"answer": answer}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))

@app.post("/analyze-resume")
def resume_analysis(request: ResumeRequest):
    try:
        result = analyze_resume(request.resume_text, request.target_role)
        return json.loads(result)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
