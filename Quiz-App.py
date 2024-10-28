class QuizApp:
    def __init__(self):
        self.questions = [
            {"question": "What is the capital of France?", "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"], "answer": "C"},
            {"question": "Which planet is known as the Red Planet?", "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"], "answer": "B"},
            {"question": "What is the smallest ocean in the world?", "options": ["A) Atlantic", "B) Indian", "C) Pacific", "D) Arctic"], "answer": "D"},
        ]
        self.score = 0

    def start_quiz(self):
        print("Welcome to the Quiz App!\n")
        for idx, q in enumerate(self.questions):
            print(f"Question {idx + 1}: {q['question']}")
            for option in q["options"]:
                print(option)
            answer = input("Your answer (A/B/C/D): ").upper()
            if answer == q["answer"]:
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is {q['answer']}\n")
        self.show_results()

    def show_results(self):
        print("Quiz completed!\n")
        print(f"Your final score is: {self.score}/{len(self.questions)}")
        if self.score == len(self.questions):
            print("Excellent work!")
        elif self.score >= len(self.questions) // 2:
            print("Good job!")
        else:
            print("Better luck next time!")

# Initialize and start the quiz
quiz = QuizApp()
quiz.start_quiz()
