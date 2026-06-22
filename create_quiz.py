import json
import random

with open("question_bank.json", "r", encoding="utf-8") as f:
    bank = json.load(f)

with open("used_questions.json", "r", encoding="utf-8") as f:
    used = json.load(f)

all_questions = bank["questions"]
used_ids = used["used_question_ids"]

available_questions = []

for q in all_questions:
    if q["id"] not in used_ids:
        available_questions.append(q)

if len(available_questions) < 5:
    print("Not enough unused questions.")
    reset_choice = input("All questions have been used. Reset used questions? Y/N: ").strip().upper()

    if reset_choice == "Y":
        used_ids = []
        available_questions = all_questions
        print("Used questions reset.")
    else:
        print("Quiz creation cancelled.")
        exit()

selected_questions = random.sample(available_questions, 5)

quiz = {
    "questions": selected_questions
}

with open("quiz.json", "w", encoding="utf-8") as f:
    json.dump(quiz, f, indent=4)

for q in selected_questions:
    used_ids.append(q["id"])

with open("used_questions.json", "w", encoding="utf-8") as f:
    json.dump({"used_question_ids": used_ids}, f, indent=4)

print("Quiz created successfully.")