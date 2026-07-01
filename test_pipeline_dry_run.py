"""
Dry-run sanity check: confirms the Crew object builds correctly without
making real API calls. Run this BEFORE adding real keys to catch wiring
issues for free.
"""
import os
os.environ.setdefault("GROQ_API_KEY", "dummy")
os.environ.setdefault("SERPER_API_KEY", "dummy")

from agents import build_research_agent, build_writer_agent, build_formatter_agent
from tasks import build_research_task, build_writing_task, build_formatting_task
from crewai import Crew, Process

research_agent = build_research_agent()
writer_agent = build_writer_agent()
formatter_agent = build_formatter_agent()

research_task = build_research_task(research_agent, "test idea", "test extras")
writing_task = build_writing_task(writer_agent, "test idea", "test extras", research_task)
formatting_task = build_formatting_task(formatter_agent, writing_task)

crew = Crew(
    agents=[research_agent, writer_agent, formatter_agent],
    tasks=[research_task, writing_task, formatting_task],
    process=Process.sequential,
)

print("Crew built successfully:")
print(f"  Agents: {[a.role for a in crew.agents]}")
print(f"  Tasks: {len(crew.tasks)}")
print("Pipeline wiring is correct. Add real API keys to .env and run crew.py for a live test.")
