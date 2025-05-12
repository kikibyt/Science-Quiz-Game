import random
import time
import tkinter as tk
from tkinter import messagebox



# Initialize Pygame for music playback


# Define the questions for Science and Geography
SCIENCE_QUESTIONS = [
    {"question": "What is the chemical symbol for water?", "answer": "H2O"},
    {"question": "What planet is known as the Red Planet?", "answer": "Mars"},
    {"question": "What force keeps us on the ground?", "answer": "Gravity"},
    {"question": "How many bones are in the adult human body?", "answer": "206"},
    {"question": "What gas do plants absorb from the atmosphere?", "answer": "Carbon Dioxide"},
]

GEOGRAPHY_QUESTIONS = [
    {"question": "What is the capital of Nigeria?", "answer": "Abuja"},
    {"question": "Which continent is Egypt located in?", "answer": "Africa"},
    {"question": "What is the longest river in the world?", "answer": "Nile"},
    {"question": "In which state is the River Niger bridge located?", "answer": "Anambra"},
    {"question": "Which country has the largest population in Africa?", "answer": "Nigeria"},
]

ALL_QUESTIONS = SCIENCE_QUESTIONS + GEOGRAPHY_QUESTIONS
TOTAL_QUESTIONS = 10

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Science & Geography Quiz")
        self.root.geometry("500x400")
        self.root.config(bg="#ffe6f0")

        self.score = 0
        self.current_question = 0
        self.questions_to_ask = self.get_random_questions(ALL_QUESTIONS, TOTAL_QUESTIONS)
        self.start_time = None

        self.create_widgets()

    def create_widgets(self):
        # Title
        self.title_label = tk.Label(self.root, text="Science & Geography Quiz", font=("Arial", 16, "bold"), bg="#ffe6f0", fg="#ff007f")
        self.title_label.pack(pady=20)

        # Question Display
        self.question_label = tk.Label(self.root, text="", font=("Arial", 14), bg="#ffe6f0", wraplength=450)
        self.question_label.pack(pady=20)

        # Answer Entry
        self.answer_entry = tk.Entry(self.root, font=("Arial", 12), width=30)
        self.answer_entry.pack(pady=10)

        # Submit Button
        self.submit_button = tk.Button(self.root, text="Submit Answer", font=("Arial", 12), bg="#ffccdf", command=self.check_answer)
        self.submit_button.pack(pady=10)

        # Start Button
        self.start_button = tk.Button(self.root, text="Start Quiz", font=("Arial", 12, "bold"), bg="#ffccdf", command=self.start_quiz)
        self.start_button.pack(pady=10)

        # Result Display
        self.result_label = tk.Label(self.root, text="", font=("Arial", 12), bg="#ffe6f0")
        self.result_label.pack(pady=10)

    def get_random_questions(self, questions, num_questions):
        random.shuffle(questions)
        return questions[:num_questions]

    def start_quiz(self):
        self.score = 0
        self.current_question = 0
        self.start_time = time.time()
        self.start_button.pack_forget()
        self.next_question()

    def next_question(self):
        if self.current_question < TOTAL_QUESTIONS:
            question_text = self.questions_to_ask[self.current_question]["question"]
            self.question_label.config(text=f"Question {self.current_question + 1}: {question_text}")
            self.answer_entry.delete(0, tk.END)
            self.result_label.config(text="")
        else:
            self.end_quiz()

    def check_answer(self):
        answer = self.answer_entry.get().strip()
        correct_answer = self.questions_to_ask[self.current_question]["answer"]

        if answer.lower() == correct_answer.lower():
            self.score += 1
            self.result_label.config(text="Correct!", fg="green")
        else:
            self.result_label.config(text=f"Incorrect! The correct answer is: {correct_answer}", fg="red")

        self.current_question += 1
        self.root.after(1500, self.next_question)

    def end_quiz(self):
        end_time = time.time()
        total_time = round(end_time - self.start_time, 2)
        messagebox.showinfo("Quiz Complete!", f"Time Taken: {total_time} seconds\nScore: {self.score}/{TOTAL_QUESTIONS}")
        self.root.destroy()

# Create the main window and run the application
root = tk.Tk()
app = QuizApp(root)
root.mainloop()
