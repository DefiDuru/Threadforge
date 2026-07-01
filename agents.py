import os
from dotenv import load_dotenv

load_dotenv()

# Fix for Groq not supporting cache_breakpoint from crewai/litellm
os.environ["LITELLM_DROP_PARAMS"] = "true"
import litellm
litellm.drop_params = True

from crewai import Agent, LLM
from crewai_tools import SerperDevTool

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env file")

groq_llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=api_key,
    temperature=0.7,
)

search_tool = SerperDevTool()


def build_research_agent() -> Agent:
    return Agent(
        role="Launch Research Analyst",
        goal=(
            "Find real, verifiable stats, comparisons, and social proof relevant "
            "to the project idea provided, so the thread has actual substance "
            "instead of invented numbers."
        ),
        backstory=(
            "You are a sharp research analyst who has read thousands of startup "
            "and crypto project launches. You know the difference between a real "
            "data point and marketing fluff, and you always flag when no solid "
            "evidence exists rather than making something up."
        ),
        tools=[search_tool],
        llm=groq_llm,
        verbose=True,
        allow_delegation=False,
    )


def build_writer_agent() -> Agent:
    return Agent(
        role="Thread Architect",
        goal=(
            "Turn a project idea plus research findings into a complete X thread "
            "that strictly follows the 9-element ThreadForge framework, with each "
            "element as its own tweet."
        ),
        backstory=(
            "You are a veteran crypto and tech Twitter ghostwriter who has written "
            "sponsored threads and creator campaigns for real projects. You know "
            "how to make a thread feel human, specific, and structured rather than "
            "generic AI output. You never use corporate buzzwords."
        ),
        llm=groq_llm,
        verbose=True,
        allow_delegation=False,
    )


def build_formatter_agent() -> Agent:
    return Agent(
        role="Thread Quality Editor",
        goal=(
            "Review the drafted thread against the 9-element framework and hard "
            "rules, fix anything that violates them, enforce character limits, "
            "and output the final clean, numbered, ready-to-post thread."
        ),
        backstory=(
            "You are a meticulous editor who has rejected hundreds of AI-sounding "
            "drafts. You check every tweet against the framework checklist before "
            "it ships, and you never let a banned phrase slip through."
        ),
        llm=groq_llm,
        verbose=True,
        allow_delegation=False,
    )
