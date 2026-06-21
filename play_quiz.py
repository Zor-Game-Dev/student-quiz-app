import json

with open("quiz.json", "r", encoding="utf-8") as f:
    data = json.load(f)

score = 0

for index, question in enumerate(data["questions"], start=1):
    print(f"\nQ{index}. {question['question']}")

    options = question["options"]

    for i, option in enumerate(options):
        print(f"{chr(65 + i)}. {option}")

    user_answer = input("Enter your answer A/B/C/D: ").strip().upper()

    if len(user_answer) != 1 or user_answer not in ["A", "B", "C", "D"]:
    print("Please enter A, B, C, or D")
    continue

    option_index = ord(user_answer) - 65

    if option_index < 0 or option_index >= len(options):
        print("Invalid option.")
        continue

    selected_option = options[option_index]

    if selected_option == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
        print("Correct answer:", question["answer"])
        print("Explanation:", question["explanation"])

print(f"\nFinal Score: {score}/{len(data['questions'])}")