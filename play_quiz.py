import json
from datetime import datetime

with open("quiz.json", "r", encoding="utf-8") as f:
    data = json.load(f)

score = 0

for index, question in enumerate(data["questions"], start=1):
    print(f"\nQ{index}. {question['question']}")

    options = question["options"]

    for i, option in enumerate(options):
        print(f"{chr(65 + i)}. {option}")

    while True:
        user_answer = input("Enter your answer A/B/C/D: (or Q to quit): ").strip().upper()

        if user_answer == "Q":
            print("Quiz exited by user.")
            exit()   

        if len(user_answer) != 1 or user_answer not in ["A", "B", "C", "D"]:
            print("Please enter A, B, C, or D")
            continue

        option_index = ord(user_answer) - 65

        if option_index < 0 or option_index >= len(options):
            print("Invalid option.")
            continue

        break

    selected_option = options[option_index]

    if selected_option == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
        print("Correct answer:", question["answer"])
        print("Explanation:", question["explanation"])

        with open("wrong_answers.json", "r", encoding="utf-8") as f:
            wrong_data = json.load(f)

        already_exists = False

        for wrong_question in wrong_data["wrong_questions"]:
            if wrong_question["question"] == question["question"]:
                already_exists = True
                break

        if not already_exists:
            wrong_data["wrong_questions"].append({
                "question": question["question"],
                "options": question["options"],
                "answer": question["answer"],
                "explanation": question["explanation"]
        })

    with open("wrong_answers.json", "w", encoding="utf-8") as f:
        json.dump(wrong_data, f, indent=4)
        
total_questions = len(data["questions"])

print(f"\nFinal Score: {score}/{total_questions}")

with open("scores.json", "r", encoding="utf-8") as f:
    scores_data = json.load(f)

scores_data["attempts"].append({
    "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "score": score,
    "total": total_questions
})

with open("scores.json", "w", encoding="utf-8") as f:
    json.dump(scores_data, f, indent=4)

print("Score saved successfully.")