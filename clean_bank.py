import json

with open("question_bank.json", "r", encoding="utf-8") as f:
    data = json.load(f)

questions = data.get("questions", [])

clean_questions = []
seen_questions = set()

for q in questions:
    if "question" not in q:
        continue

    if "options" not in q or len(q["options"]) != 4:
        continue

    if "answer" not in q or q["answer"] not in q["options"]:
        continue

    if "explanation" not in q:
        continue

    question_text = q["question"].strip().lower()

    if question_text in seen_questions:
        continue

    seen_questions.add(question_text)

    q["id"] = len(clean_questions) + 1
    clean_questions.append(q)

    if len(clean_questions) == 10:
        break

with open("question_bank.json", "w", encoding="utf-8") as f:
    json.dump({"questions": clean_questions}, f, indent=4)

print(f"Cleaned question bank saved with {len(clean_questions)} valid questions.")