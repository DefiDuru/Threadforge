from crewai import Task
from framework import THREAD_FRAMEWORK, FRAMEWORK_RULES


def build_research_task(agent, project_idea: str, extra_requirements: str) -> Task:
    return Task(
        description=(
            f"Project idea / announcement:\n{project_idea}\n\n"
            f"Extra project-specific requirements (if any):\n{extra_requirements}\n\n"
            "Search the live web for real, relevant facts that could serve as "
            "social proof in a launch thread for THIS specific project. "
            "Focus your searches on: AI agent tools market size and growth, "
            "Twitter/X thread engagement stats, content creation tool adoption rates, "
            "crypto launchpad activity, and builder/creator economy stats. "
            "Do NOT search for the literal product name as if it is an existing market. "
            "Return a short bullet list of findings, each tagged VERIFIED (found a "
            "direct source), REPORTED (mentioned but not directly confirmed), or "
            "ASSUMPTION (no source found, reasonable inference only). "
            "Do not invent numbers."
        ),
        expected_output=(
            "A bullet list of 3-6 research findings relevant to AI tools, content "
            "creation, or crypto builder ecosystem, each tagged VERIFIED, REPORTED, "
            "or ASSUMPTION, with a one-line note on where it came from."
        ),
        agent=agent,
    )


def build_writing_task(agent, project_idea: str, extra_requirements: str, research_task: Task) -> Task:
    return Task(
        description=(
            f"Project idea / announcement:\n{project_idea}\n\n"
            f"Extra project-specific requirements (if any):\n{extra_requirements}\n\n"
            f"{THREAD_FRAMEWORK}\n\n{FRAMEWORK_RULES}\n\n"
            "Using the research findings from the previous task, draft a complete "
            "X thread following the 9-element framework above. Use the VERIFIED "
            "findings for the social proof tweet; if nothing is VERIFIED, use a "
            "concrete mechanism detail from the project idea instead of inventing "
            "a stat. Layer in any extra project-specific requirements without "
            "dropping any of the 9 core elements."
        ),
        expected_output=(
            "A numbered draft thread (9+ tweets), one element per tweet, in order."
        ),
        agent=agent,
        context=[research_task],
    )


def build_formatting_task(agent, writing_task: Task) -> Task:
    return Task(
        description=(
            "Review the drafted thread against the 9-element framework and hard "
            "rules. Check: every element present as its own tweet, no banned "
            "AI-tell phrases, each tweet under 280 characters, correct numbering "
            "format. Fix any violations. Output ONLY the final clean thread, "
            "numbered, ready to copy and post — no preamble, no explanation."
        ),
        expected_output=(
            "The final, ready-to-post X thread as plain numbered tweets, nothing else."
        ),
        agent=agent,
        context=[writing_task],
    )
