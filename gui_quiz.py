import json
import customtkinter as ctk
from datetime import datetime

with open("quiz.json", "r", encoding="utf-8") as f:
    data = json.load(f)

questions = data["questions"]
current_index = 0
score = 0
selected_answer = None

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Take Quiz")
app.geometry("700x550")

title_label = ctk.CTkLabel(app, text="Quiz", font=("Arial", 26, "bold"))
title_label.pack(pady=20)

question_label = ctk.CTkLabel(app, text="", font=("Arial", 18), wraplength=600)
question_label.pack(pady=20)

option_buttons = []

feedback_label = ctk.CTkLabel(app, text="", font=("Arial", 16), wraplength=600)
feedback_label.pack(pady=20)

def load_question():
    global selected_answer

    selected_answer = None
    feedback_label.configure(text="")

    question = questions[current_index]
    question_label.configure(text=f"Q{current_index + 1}. {question['question']}")

    for button in option_buttons:
        button.destroy()

    option_buttons.clear()

    for option in question["options"]:
        btn = ctk.CTkButton(
            app,
            text=option,
            width=500,
            command=lambda opt=option: select_answer(opt)
        )
        btn.pack(pady=5)
        option_buttons.append(btn)

def select_answer(option):
    global selected_answer
    selected_answer = option

    for button in option_buttons:
        if button.cget("text") == option:
            button.configure(fg_color="green")
        else:
            button.configure(fg_color="#1f6aa5")

def submit_answer():
    global score, current_index

    if selected_answer is None:
        feedback_label.configure(text="Please select an answer.")
        return

    question = questions[current_index]

    if selected_answer == question["answer"]:
        feedback_label.configure(text="Correct!")
        score += 1
    else:
        feedback_label.configure(
            text=f"Wrong!\nCorrect Answer: {question['answer']}\nExplanation: {question['explanation']}"
        )

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

    submit_button.configure(state="disabled")
    next_button.configure(state="normal")

def next_question():
    global current_index

    current_index += 1

    if current_index >= len(questions):
        finish_quiz()
    else:
        submit_button.configure(state="normal")
        next_button.configure(state="disabled")
        load_question()

def finish_quiz():
    total_questions = len(questions)

    with open("scores.json", "r", encoding="utf-8") as f:
        scores_data = json.load(f)

    scores_data["attempts"].append({
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "score": score,
        "total": total_questions
    })

    with open("scores.json", "w", encoding="utf-8") as f:
        json.dump(scores_data, f, indent=4)

    for button in option_buttons:
        button.destroy()

    submit_button.destroy()
    next_button.destroy()

    question_label.configure(text="Quiz Completed")
    feedback_label.configure(text=f"Final Score: {score}/{total_questions}\nScore saved successfully.")

submit_button = ctk.CTkButton(app, text="Submit Answer", command=submit_answer)
submit_button.pack(pady=10)

next_button = ctk.CTkButton(app, text="Next Question", command=next_question, state="disabled")
next_button.pack(pady=10)

exit_button = ctk.CTkButton(app, text="Exit", command=app.destroy)
exit_button.pack(pady=20)

load_question()

app.mainloop()