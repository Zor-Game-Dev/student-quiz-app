import json

with open("scores.json", "r", encoding="utf-8") as f:
    data = json.load(f)

attempts = data["attempts"]

if len(attempts) == 0:
    print("No quiz attempts found.")
else:
    total_attempts = len(attempts)

    percentages = []

    for attempt in attempts:
        percentage = (attempt["score"] / attempt["total"]) * 100
        percentages.append(percentage)

    average_percentage = sum(percentages) / total_attempts
    best_attempt = max(attempts, key=lambda x: x["score"])

    print("\n===== QUIZ STATISTICS =====")
    print(f"Total Attempts: {total_attempts}")
    print(f"Best Score: {best_attempt['score']}/{best_attempt['total']}")
    print(f"Average Score: {average_percentage:.2f}%")

    print("\n===== PREVIOUS SCORES =====")

    for i, attempt in enumerate(attempts, start=1):
        percentage = (attempt["score"] / attempt["total"]) * 100

        print(f"\nAttempt {i}")
        print(f"Date: {attempt['date']}")
        print(f"Score: {attempt['score']}/{attempt['total']} ({percentage:.2f}%)")