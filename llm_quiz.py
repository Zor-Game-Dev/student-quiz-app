import fitz
import requests
import json

def extract_json(text):
    start = text.find("{")
    end = text.rfind("}")

    if start == -1 or end == -1:
        raise ValueError("No JSON object found in model response")

    return text[start:end + 1]

pdf = fitz.open("sample.pdf")

full_text = ""

for page in pdf:
    full_text += page.get_text()

notes = full_text[:3000]

prompt = f"""
Generate exactly 5 MCQ questions from the notes.

STRICT RULES:
- Do NOT use A, B, C, D as option values.
- Each option must be a meaningful phrase.
- The answer must exactly match one option.
- Avoid repeated questions.
- Return only JSON.

Bad example:
"options": ["A", "B", "C", "D"]

Good example:
"options": [
  "A distributed version control system",
  "A database management system",
  "A programming language",
  "A web browser"
]

JSON format:
{{
  "questions": [
    {{
      "question": "What is Git?",
      "options": [
        "A distributed version control system",
        "A database management system",
        "A programming language",
        "A web browser"
      ],
      "answer": "A distributed version control system",
      "explanation": "Git is used to track changes in files and manage versions."
    }}
  ]
}}

Notes:
{notes}
"""

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3:8b",   
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.2
        }
    }
)

result = response.json()

clean_json = extract_json(result["response"])

with open("quiz.json", "w", encoding="utf-8") as f:
    f.write(clean_json)

print("Quiz saved to quiz.json")