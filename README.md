# ThreadForge

A multi-agent AI system that turns a raw project idea into a launch-ready X
thread, built on a proven 9-element thread structure with live web research
for real social proof.

Built for the HACD Labs Incubator Season 2 (GrowStreams), backing the FORGE
utility Stack Token.

## How it works

Three CrewAI agents run in sequence, powered by Groq's `llama-3.3-70b-versatile`:

1. **Research Agent** — searches the live web (SerperDev) for real, citable
   facts and social proof relevant to the project idea. Flags every finding
   as VERIFIED, REPORTED, or ASSUMPTION so nothing gets invented.
2. **Writer Agent** — drafts the thread using ThreadForge's 9-element
   framework (hook, question, problem, solution flow, social proof, human
   structure, personal touch, use cases, CTA), one element per tweet.
3. **Formatter Agent** — reviews the draft against the framework's hard rules
   (character limits, banned AI-tell phrases, correct structure) and outputs
   the final ready-to-post thread.

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env   # then add your real GROQ_API_KEY and SERPER_API_KEY
```

Get a free Groq API key at https://console.groq.com
Get a SerperDev API key at https://serper.dev

## Run as a script

```bash
python3 crew.py
```

## Run as an API

```bash
uvicorn main:app --reload --port 8000
```

Then POST to `/generate-thread`:

```bash
curl -X POST http://localhost:8000/generate-thread \
  -H "Content-Type: application/json" \
  -d '{
    "project_idea": "Describe your project in a few sentences here.",
    "extra_requirements": "Tag @YourHandle. Include #YourHashtag."
  }'
```

## Project structure

```
threadforge/
├── framework.py    # The 9-element thread framework (core IP)
├── agents.py       # Research, Writer, Formatter agent definitions
├── tasks.py        # Task definitions wiring agents together
├── crew.py         # Sequential crew orchestration + CLI entrypoint
├── main.py         # FastAPI service exposing /generate-thread
├── requirements.txt
└── .env.example
```

## Roadmap (planned, not yet built)

- Support for additional platforms beyond X
- Custom brand voice training per project
- Higher research-agent usage tiers for FORGE holders

## Deploy

### Render
A `render.yaml` is included. On Render: New + Blueprint, point at this repo,
add your `GROQ_API_KEY` and `SERPER_API_KEY` as environment variables when
prompted. Render reads everything else from `render.yaml`.

### Vercel (alternative)
Wrap `main:app` with a Vercel Python serverless entrypoint, or deploy the
FastAPI app via a `vercel.json` using `@vercel/python`. Render is the simpler
path for a FastAPI service with no rewrite needed.
