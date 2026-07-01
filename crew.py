from dotenv import load_dotenv
load_dotenv()

from crewai import Crew, Process
from agents import build_research_agent, build_writer_agent, build_formatter_agent
from tasks import build_research_task, build_writing_task, build_formatting_task


def run_threadforge(project_idea: str, extra_requirements: str = "") -> str:
    research_agent = build_research_agent()
    writer_agent = build_writer_agent()
    formatter_agent = build_formatter_agent()

    research_task = build_research_task(research_agent, project_idea, extra_requirements)
    writing_task = build_writing_task(writer_agent, project_idea, extra_requirements, research_task)
    formatting_task = build_formatting_task(formatter_agent, writing_task)

    crew = Crew(
        agents=[research_agent, writer_agent, formatter_agent],
        tasks=[research_task, writing_task, formatting_task],
        process=Process.sequential,
        verbose=True,
    )

    result = crew.kickoff()
    return str(result)


if __name__ == "__main__":
    idea = (
        "ThreadForge: a multi-agent AI system that turns a raw project idea into "
        "a launch-ready X thread using a proven 9-element structure and live "
        "research for real social proof. Launching as a FORGE Stack Asset on "
        "HACD during Incubator Season 2."
    )
    extra = "Tag @GrowwStreams. Mention it is launching on HACD Launchpad."
    print(run_threadforge(idea, extra))
