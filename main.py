from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from crew import run_threadforge

app = FastAPI(
    title="ThreadForge API",
    description=(
        "Multi-agent AI system that turns a project idea into a launch-ready "
        "X thread using a proven 9-element structure and live research."
    ),
    version="0.1.0",
)
# CORS configuration
origins = [
    "https://threadforge-onchain.lovable.app",
    "http://localhost:3000",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ThreadRequest(BaseModel):
    project_idea: str = Field(
        ..., min_length=10,
        description="A few sentences describing the project or announcement."
    )
    extra_requirements: str = Field(
        default="",
        description="Optional project-specific extras: hashtags, mentions, min tweet count, etc."
    )


class ThreadResponse(BaseModel):
    thread: str


@app.get("/health")
def health():
    return {"status": "ok", "service": "ThreadForge"}


@app.post("/generate-thread", response_model=ThreadResponse)
def generate_thread(req: ThreadRequest):
    try:
        thread = run_threadforge(req.project_idea, req.extra_requirements)
        return ThreadResponse(thread=thread)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Run with: uvicorn main:app --reload --port 8000
import importlib.metadata

@app.get("/versions")
def versions():
    return {
        "crewai": importlib.metadata.version("crewai"),
        "litellm": importlib.metadata.version("litellm"),
        "fastapi": importlib.metadata.version("fastapi"),
        "groq": importlib.metadata.version("groq"),
    }
    import inspect
from crewai import LLM

@app.get("/llm-info")
def llm_info():
    return {
        "llm_signature": str(inspect.signature(LLM)),
    }