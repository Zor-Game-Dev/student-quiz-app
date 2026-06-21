import json

def validate_quiz(file_path="quiz.json"):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if "questions" not in data:
        print("Invalid: missing questions")
        return False

    for i, q in enumerate(data["questions"], start=1):
        if "question" not in q:
            print(f"Q{i}: missing question")
            return False

        if "options" not in q or len(q["options"]) != 4:
            print(f"Q{i}: must have exactly 4 options")
            return False

        if "answer" not in q:
            print(f"Q{i}: missing answer")
            return False

        if q["answer"] not in q["options"]:
            print(f"Q{i}: answer is not in options")
            return False

        if "explanation" not in q:
            print(f"Q{i}: missing explanation")
            return False

    print("Quiz JSON is valid")
    return True


validate_quiz()