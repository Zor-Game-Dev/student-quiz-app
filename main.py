import fitz
from quiz_generator import generate_mcqs

pdf = fitz.open("sample.pdf")

full_text = ""

for page in pdf:
    full_text += page.get_text()

questions = generate_mcqs(full_text)

for i, q in enumerate(questions, start=1):
    print(f"\nQ{i}. {q['question']}")
    print("Options:")

    for option in q["options"]:
        print("-", option)

    print("Answer:", q["answer"])