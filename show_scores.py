import json

with open("scores.json", "r", encoding="utf-8") as f:
    data = json.load(f)

attempts = data["attempts"]

if len(attempts) == 0:
    print("No quiz attempts found.")
else:
    print("\n===== PREVIOUS SCORES =====")

    for i, attempt in enumerate(attempts, start=1):
        print(f"{i}. Date: {attempt['date']}")
        print(f"   Score: {attempt['score']}/{attempt['total']}")   