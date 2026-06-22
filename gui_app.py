import customtkinter as ctk
import subprocess
import threading

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Student Quiz App")
app.geometry("500x500")

title = ctk.CTkLabel(app, text="Student Quiz App", font=("Arial", 26, "bold"))
title.pack(pady=30)

output_box = ctk.CTkTextbox(app, width=420, height=180)
output_box.pack(pady=20)


def write_output(text):
    output_box.insert("end", text)
    output_box.see("end")


def run_script(script_name):
    app.after(0, lambda: write_output(f"\nRunning {script_name}...\n"))

    result = subprocess.run(
        ["python", script_name],
        capture_output=True,
        text=True
    )

    if result.stdout:
        app.after(0, lambda: write_output(result.stdout))

    if result.stderr:
        app.after(0, lambda: write_output("\nERROR:\n" + result.stderr))


def run_scripts_in_thread(scripts):
    output_box.delete("1.0", "end")

    def task():
        for script in scripts:
            run_script(script)
        app.after(0, lambda: write_output("\nDone.\n"))

    threading.Thread(target=task, daemon=True).start()


def generate_quiz():
    run_scripts_in_thread([
        "llm_quiz.py",
        "validate_bank.py",
        "clean_bank.py",
        "create_quiz.py"
    ])


def take_quiz():
    run_scripts_in_thread(["gui_quiz.py"])


def show_scores():
    run_scripts_in_thread(["show_scores.py"])


def show_wrong_answers():
    run_scripts_in_thread(["show_wrong_answers.py"])


def revision_quiz():
    run_scripts_in_thread(["revision_quiz.py"])


ctk.CTkButton(app, text="Generate Quiz from PDF", command=generate_quiz).pack(pady=8)
ctk.CTkButton(app, text="Take Quiz", command=take_quiz).pack(pady=8)
ctk.CTkButton(app, text="Show Scores", command=show_scores).pack(pady=8)
ctk.CTkButton(app, text="Show Wrong Answers", command=show_wrong_answers).pack(pady=8)
ctk.CTkButton(app, text="Revision Quiz", command=revision_quiz).pack(pady=8)
ctk.CTkButton(app, text="Exit", command=app.destroy).pack(pady=20)

app.mainloop()