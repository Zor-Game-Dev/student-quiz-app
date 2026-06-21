import os

def show_menu():
    print("\n===== STUDENT QUIZ APP =====")
    print("1. Generate Quiz from PDF")
    print("2. Validate Quiz")
    print("3. Take Quiz")
    print("4. Exit")

while True:
    show_menu()

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        print("\nGenerating quiz from PDF...")
        os.system("python llm_quiz.py")

    elif choice == "2":
        print("\nValidating quiz...")
        os.system("python validator.py")

    elif choice == "3":
        print("\nStarting quiz...")
        os.system("python play_quiz.py")

    elif choice == "4":
        print("Exiting app.")
        break

    else:
        print("Invalid choice. Enter 1, 2, 3, or 4.")