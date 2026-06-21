import random

def generate_mcqs(text):
    sentences = text.split(".")
    questions = []

    for sentence in sentences:
        sentence = sentence.strip()

        if len(sentence.split()) > 6:
            words = sentence.split()
            answer = random.choice(words)

            question_text = sentence.replace(answer, "_____")

            question = {
                "question": question_text,
                "options": [
                    answer,
                    "Python",
                    "Database",
                    "Internet"
                ],
                "answer": answer
            }

            questions.append(question)

        if len(questions) == 5:
            break

    return questions