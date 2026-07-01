"""
ThreadForge's core IP: the 9-element thread framework.
Every thread the writer agent produces must hit each of these as its OWN tweet.
"""

THREAD_FRAMEWORK = """
You must structure every thread using exactly these 9 elements, each as its own
individual tweet, in this order. Do not skip, merge, or reorder any element.

1. HOOK — A great, relatable opening line. Must stop the scroll. No generic
   "Excited to announce" energy. Lead with tension, a surprising fact, or a
   sharp observation the reader will recognize from their own life.

2. QUESTION — A clear, relatable question that pulls the reader into the
   problem space. Should feel like something the reader has actually asked
   themselves.

3. PROBLEM — A clear, relatable problem statement. Name the pain specifically.
   Avoid vague corporate language ("inefficiencies exist") in favor of concrete,
   visceral framing ("you've spent 3 hours rewriting the same paragraph").

4. SOLUTION FLOW — How the project solves the problem, explained as a clean,
   logical sequence. Walk the reader through it like you're explaining it to a
   smart friend, not pitching a board.

5. SOCIAL PROOF — Evidence the thing is real and works: stats, user counts,
   benchmark numbers, or a verified quote. This is where the research agent's
   findings get used. No invented numbers — if no real data is available, use a
   concrete mechanism detail instead of a fake statistic.

6. HUMAN STRUCTURE — A tweet that explicitly breaks the "AI voice" pattern:
   short, punchy, maybe a single aside or bit of personality. Avoid em-dashes,
   avoid "Moreover," "Furthermore," "In today's world." Write like a person who
   is tired and a little proud of what they built.

7. PERSONAL TOUCH — A first-person moment: why you built this, what surprised
   you, a small admission or behind-the-scenes detail. This is the tweet that
   makes the thread feel like it came from a specific human.

8. USE CASES — 2-4 concrete, specific scenarios of who uses this and how.
   Name a persona or situation, not a feature list.

9. CTA — A strong, specific call to action. Not "check it out" — tell the
   reader exactly what to do and why now (try it, follow for updates, reply
   with their use case, join the waitlist, etc).
"""

FRAMEWORK_RULES = """
Hard rules for every thread:
- Each of the 9 elements is its OWN tweet (9 tweets minimum for the core thread).
- No tweet should restate a previous tweet's point.
- Avoid AI-tell phrases: "Moreover", "Furthermore", "In today's fast-paced world",
  "game-changer", "revolutionize", "seamlessly", "unlock the power of".
- Keep each tweet under 280 characters.
- Numbering format: "1/", "2/", etc. at the start of each tweet.
- If the project has explicit extra requirements (tags, hashtags, minimum tweet
  count, required mentions), layer those on top of the 9-element core without
  removing any of the 9 elements.
"""
