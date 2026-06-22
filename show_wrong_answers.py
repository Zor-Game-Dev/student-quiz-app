import json

with open("wrong_answers.json", "r", encoding="utf-8") as f:
    data = json.load(f)

wrong_questions = data["wrong_questions"]

if len(wrong_questions) == 0:
    print("No wrong answers found.")
else:
    print("\n===== WRONG ANSWERS =====")

    for i, question in enumerate(wrong_questions, start=1):
        print(f"\nQuestion {i}")
        print("Question :", question["question"])
        print("Answer   :", question["answer"])
        print("Explanation :", question["explanation"])