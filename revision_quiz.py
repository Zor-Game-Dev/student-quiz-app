import json
import random

with open("wrong_answers.json", "r", encoding="utf-8") as f:
    wrong_data = json.load(f)

wrong_questions = wrong_data["wrong_questions"]

if len(wrong_questions) == 0:
    print("No wrong answers available for revision.")
    exit()

revision_questions = random.sample(wrong_questions, min(5, len(wrong_questions)))

score = 0
still_wrong = []

print("\n===== REVISION QUIZ =====")

for index, question in enumerate(revision_questions, start=1):
    print(f"\nQ{index}. {question['question']}")

    options = question["options"]

    for i, option in enumerate(options):
        print(f"{chr(65 + i)}. {option}")

    while True:
        user_answer = input("Enter your answer A/B/C/D (or Q to quit): ").strip().upper()

        if user_answer == "Q":
            print("Revision quiz exited.")
            exit()

        if len(user_answer) != 1 or user_answer not in ["A", "B", "C", "D"]:
            print("Please enter A, B, C, D or Q")
            continue

        option_index = ord(user_answer) - 65
        break

    selected_option = options[option_index]

    if selected_option == question["answer"]:
        print("Correct! Removed from wrong answers.")
        score += 1
    else:
        print("Wrong!")
        print("Correct answer:", question["answer"])
        print("Explanation:", question["explanation"])
        still_wrong.append(question)

remaining_wrong = []

for question in wrong_questions:
    if question not in revision_questions:
        remaining_wrong.append(question)

remaining_wrong.extend(still_wrong)

with open("wrong_answers.json", "w", encoding="utf-8") as f:
    json.dump({"wrong_questions": remaining_wrong}, f, indent=4)

print(f"\nRevision Score: {score}/{len(revision_questions)}")