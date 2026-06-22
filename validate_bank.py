import json

with open("question_bank.json", "r", encoding="utf-8") as f:
    data = json.load(f)

questions = data.get("questions", [])

valid_count = 0

for i, q in enumerate(questions, start=1):
    errors = []

    if "question" not in q:
        errors.append("missing question")

    if "options" not in q or len(q["options"]) != 4:
        errors.append("must have exactly 4 options")

    if "answer" not in q:
        errors.append("missing answer")
    elif q["answer"] not in q.get("options", []):
        errors.append("answer is not in options")

    if "explanation" not in q:
        errors.append("missing explanation")

    if errors:
        print(f"Q{i} invalid: {', '.join(errors)}")
    else:
        valid_count += 1

print(f"\nTotal Questions: {len(questions)}")
print(f"Valid Questions: {valid_count}")
print(f"Invalid Questions: {len(questions) - valid_count}")