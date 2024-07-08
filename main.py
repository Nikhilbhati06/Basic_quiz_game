def ask_question(question, options, correct_answer):
    print(question)
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")
    
    while True:
        try:
            user_answer = int(input("Please enter the number of your answer: "))
            if 1 <= user_answer <= len(options):
                break
            else:
                print("Invalid option. Please enter a number corresponding to one of the choices.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    if options[user_answer - 1] == correct_answer:
        print("Correct!\n")
        return True
    else:
        print(f"Incorrect. The correct answer was: {correct_answer}\n")
        return False

def run_quiz(questions):
    score = 0
    for question, options, correct_answer in questions:
        if ask_question(question, options, correct_answer):
            score += 1
    
    print(f"Your final score is {score} out of {len(questions)}.")

def main():
    questions = [
        ("What is the capital of India?", ["bengal", "Delhi", "Berlin", "mumbai"], "Delhi"),
        ("What is 2 + 2?", ["3", "4", "5", "6"], "4"),
        ("Which planet is known as the BLUE Planet?", ["Earth", "Mars", "Jupiter", "Venus"], "Earth"),
    ]
    
    run_quiz(questions)

if __name__ == "__main__":
    main()
