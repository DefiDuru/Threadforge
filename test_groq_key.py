from dotenv import load_dotenv
import os
import requests

load_dotenv()
key = os.getenv("GROQ_API_KEY")
print("Key found:", key[:8] + "..." if key else "NONE")

r = requests.post(
    "https://api.groq.com/openai/v1/chat/completions",
    headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
    json={"model": "llama-3.3-70b-versatile", "messages": [{"role": "user", "content": "say hi"}]}
)
print("Status:", r.status_code)
print("Response:", r.json())
