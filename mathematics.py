import random
import time
import tkinter as tk
from tkinter import ttk, messagebox
import pygame
from moviepy.editor import VideoFileClip
import cv2
from PIL import Image, ImageTk

# Initialize Pygame for sound playback
pygame.init()
pygame.mixer.init()

# Load the background music and play it on a loop
CHEER_SOUND = "CROWD CHEER SOUND EFFECT.mp3"  # Replace with your cheer sound file
pygame.mixer.music.load("gamemusic.mp3")
pygame.mixer.music.play(-1)

# Define the questions for Science and Geography
SCIENCE_QUESTIONS = [
    {"question": "What is the chemical symbol for water?", "options": ["H2O", "O2"], "answer": "H2O"},
    {"question": "What planet is known as the Red Planet?", "options": ["Earth", "Mars"], "answer": "Mars"},
    {"question": "What force keeps us on the ground?", "options": ["Magnetism", "Gravity"], "answer": "Gravity"},
    {"question": "How many bones are in the adult human body?", "options": ["206", "201"], "answer": "206"},
    {"question": "What gas do plants absorb from the atmosphere?", "options": ["Oxygen", "Carbon Dioxide"], "answer": "Carbon Dioxide"},

    # Science Questions
    {"question": "What is the chemical symbol for water?", "options": ["H2O", "O2"], "answer": "H2O"},
    {"question": "What planet is known as the Red Planet?", "options": ["Earth", "Mars"], "answer": "Mars"},
    {"question": "What is the powerhouse of the cell?", "options": ["Mitochondria", "Nucleus"], "answer": "Mitochondria"},
    {"question": "What gas do plants absorb for photosynthesis?", "options": ["Oxygen", "Carbon Dioxide"], "answer": "Carbon Dioxide"},
    {"question": "Which planet is closest to the Sun?", "options": ["Mercury", "Venus"], "answer": "Mercury"},
    
    # Computer Science Questions
    {"question": "What does CPU stand for?", "options": ["Central Processing Unit", "Computer Power Unit"], "answer": "Central Processing Unit"},
    {"question": "Which language is primarily used for web development?", "options": ["Python", "JavaScript"], "answer": "JavaScript"},
    {"question": "What is the binary representation of 2?", "options": ["10", "11"], "answer": "10"},
    {"question": "What does RAM stand for?", "options": ["Random Access Memory", "Read-Only Memory"], "answer": "Random Access Memory"},
    {"question": "Which device is used for primary storage?", "options": ["Hard Drive", "Printer"], "answer": "Hard Drive"},
    
    # Agriculture Questions
    {"question": "What is the primary purpose of crop rotation?", "options": ["Pest control", "Soil fertilization"], "answer": "Soil fertilization"},
    {"question": "Which type of soil is best for growing crops?", "options": ["Clay", "Loam"], "answer": "Loam"},
    {"question": "What is used to increase soil fertility?", "options": ["Fertilizer", "Water"], "answer": "Fertilizer"},
    {"question": "Which farming method helps conserve water?", "options": ["Drip irrigation", "Flood irrigation"], "answer": "Drip irrigation"},
    {"question": "Which crop is known as a cereal?", "options": ["Rice", "Tomato"], "answer": "Rice"},
    
    # Geography Questions
    {"question": "Which is the largest continent?", "options": ["Asia", "Africa"], "answer": "Asia"},
    {"question": "What is the capital of Nigeria?", "options": ["Lagos", "Abuja"], "answer": "Abuja"},
    {"question": "Which river is the longest in the world?", "options": ["Nile", "Amazon"], "answer": "Nile"},
    {"question": "Which ocean is the largest?", "options": ["Pacific", "Atlantic"], "answer": "Pacific"},
    {"question": "What is the smallest country in the world?", "options": ["Vatican City", "Monaco"], "answer": "Vatican City"},
    
    # Physics Questions
    {"question": "What force pulls objects toward the Earth?", "options": ["Gravity", "Magnetism"], "answer": "Gravity"},
    {"question": "What is the unit of force?", "options": ["Newton", "Joule"], "answer": "Newton"},
    {"question": "What is the speed of light?", "options": ["300,000 km/s", "150,000 km/s"], "answer": "300,000 km/s"},
    {"question": "Who developed the theory of relativity?", "options": ["Albert Einstein", "Isaac Newton"], "answer": "Albert Einstein"},
    {"question": "What is the main source of energy for Earth?", "options": ["Sun", "Moon"], "answer": "Sun"},
    
    # Chemistry Questions
    {"question": "What is the pH of neutral water?", "options": ["7", "5"], "answer": "7"},
    {"question": "What gas is produced by plants during photosynthesis?", "options": ["Oxygen", "Carbon Dioxide"], "answer": "Oxygen"},
    {"question": "Which element has the atomic number 1?", "options": ["Hydrogen", "Helium"], "answer": "Hydrogen"},
    {"question": "What is the main component of natural gas?", "options": ["Methane", "Ethane"], "answer": "Methane"},
    {"question": "What is the symbol for gold?", "options": ["Au", "Ag"], "answer": "Au"},
    
    # Biology Questions
    {"question": "What is the basic unit of life?", "options": ["Cell", "Atom"], "answer": "Cell"},
    {"question": "Which organ pumps blood throughout the body?", "options": ["Heart", "Liver"], "answer": "Heart"},
    {"question": "What do plants use to make food?", "options": ["Photosynthesis", "Respiration"], "answer": "Photosynthesis"},
    {"question": "What part of the plant absorbs water?", "options": ["Roots", "Leaves"], "answer": "Roots"},
    {"question": "What genetic material is found in cells?", "options": ["DNA", "RNA"], "answer": "DNA"},

    # Additional Questions
    {"question": "What is the largest organ in the human body?", "options": ["Skin", "Liver"], "answer": "Skin"},
    {"question": "Which gas is most abundant in Earth's atmosphere?", "options": ["Nitrogen", "Oxygen"], "answer": "Nitrogen"},
    {"question": "Which element is essential for building strong bones?", "options": ["Calcium", "Iron"], "answer": "Calcium"},
    {"question": "Who is known as the father of computers?", "options": ["Charles Babbage", "Alan Turing"], "answer": "Charles Babbage"},
    {"question": "What is the binary code for the decimal number 5?", "options": ["101", "110"], "answer": "101"}
]


GEOGRAPHY_QUESTIONS = [
    {"question": "What is the capital of Nigeria?", "options": ["Lagos", "Abuja"], "answer": "Abuja"},
    {"question": "Which continent is Egypt located in?", "options": ["Africa", "Asia"], "answer": "Africa"},
    {"question": "What is the longest river in the world?", "options": ["Amazon", "Nile"], "answer": "Nile"},
    {"question": "In which state is the River Niger bridge located?", "options": ["Anambra", "Lagos"], "answer": "Anambra"},
    {"question": "Which country has the largest population in Africa?", "options": ["Nigeria", "South Africa"], "answer": "Nigeria"},
]

ALL_QUESTIONS = SCIENCE_QUESTIONS + GEOGRAPHY_QUESTIONS
TOTAL_QUESTIONS = 50

class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Loretto Special Science Quiz")
        self.geometry("1800x980")
        self.config(bg="#ffe6f0")

        self.bg_image = tk.PhotoImage(file="bggg.png")  # Replace with your PNG image file path
        self.bg_label = tk.Label(self, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)  # This stretches the background to cover the whole window

        self.score = 0
        self.coins = 0
        self.current_question = 0
        self.questions_to_ask = self.get_random_questions(ALL_QUESTIONS, TOTAL_QUESTIONS)
        self.start_time = None

        # Coin earning system
        self.coins_earned = 0
        self.total_coins = 100

        # Labels and Progress Bar
        self.coin_label = tk.Label(self, text=f"Coins Earned: {self.coins_earned}", font=("Arial", 14), fg="#006400")
        self.coin_label.pack(pady=10)


        self.progress = ttk.Progressbar(self, length=300, mode='determinate', maximum=self.total_coins)
        self.progress.pack(pady=20)

        # Button to simulate earning coins
        self.earn_coin_button = tk.Button(self, text="Earn Coin", command=self.earn_coin)
        self.earn_coin_button.pack(pady=10)

        # Coin icon (simulated with a label)
        self.coin_icon = tk.Label(self, text="💰", fg="#006400",  font=("Arial", 20))
        self.coin_icon.pack(pady=10)
        

        self.show_intro_screen()

    def earn_coin(self):
        """Simulate earning a coin."""
        self.coins_earned += 1
        self.coin_label.config(text=f"Coins Earned: {self.coins_earned}")
        self.progress['value'] = self.coins_earned

        # Simulate animation (moving coin icon)
        self.animate_coin()

    def animate_coin(self):
        """Move the coin icon to simulate animation (like bouncing)."""
        for i in range(5):
            self.coin_icon.place(x=50 * i, y=100)
            self.update()
            time.sleep(0.05)
            self.coin_icon.place(x=50 * (5 - i), y=100)
            self.update()
            time.sleep(0.05)

    def show_intro_screen(self):
        """Show the intro screen with a video and welcome message."""
        self.play_video("lor cart.mp4")

        # Display the welcome title and "Start Quiz" button
        self.title_label = tk.Label(
            self, text="WELCOME TO LORETTO'S SPECIAL SCIENCE QUIZ",
            font=("Arial", 40, "bold"), bg="white", fg="#006400"
        )
        self.title_label.pack(pady=20)

        self.start_button = tk.Button(
            self, text="Start Quiz", font=("Arial", 44, "bold"),
            bg="darkgreen", command=self.start_quiz
        )
        self.start_button.pack(pady=20)

    def play_video(self, video_path):
        """Play an intro video in windowed mode with audio using moviepy and pygame."""
        clip = VideoFileClip(video_path).resize(height=950)

        # Pause background music while video is playing
        pygame.mixer.music.pause()

        # Set up the pygame display to 600x500 resolution
        pygame.display.set_caption("Intro Video")
        screen = pygame.display.set_mode((1800,950))

        # Play the video without fullscreen
        clip.preview()
        clip.close()

        # Resume background music after video ends
        pygame.mixer.music.unpause()
        pygame.display.quit()

    def create_widgets(self):
        """Create the main quiz interface after intro."""
        self.start_button.pack_forget()
        self.title_label.pack_forget()

        # Title
        self.title_label = tk.Label(self, text="LORETTO SPECIAL SCIENCE QUIZ", font=("Arial", 34, "bold"), bg="white", fg="#006400")
        self.title_label.pack(pady=20)

        # Question Display
        self.question_label = tk.Label(self, text="", font=("Arial", 24, "bold"), bg="white", wraplength=450)
        self.question_label.pack(pady=20)
        self.option_buttons = []
        for i in range(2):  # There will be 4 options per question
            option_button = tk.Button(self, text="", font=("Arial", 18, "bold"), bg="#ffccdf", command=lambda i=i: self.check_answer(i))
            option_button.pack(pady=10)
            self.option_buttons.append(option_button)
        # Answer Entry
     

        # Submit Button
        
        
        self.submit_button = tk.Button(self, text="Submit Answer", font=("Arial", 24, "bold"), bg="#ffccdf", command=lambda: self.check_answer(None))
        # Timer Label
        self.timer_label = tk.Label(self, text="Time: 0.00", font=("Arial", 20, "bold"), bg="#ffe6f0")
        self.timer_label.pack(pady=20)

        # Prize Display (Side Panel)
        self.prize_label = tk.Label(self, text="Coins: 0", font=("Arial", 20, "bold"), fg="darkgreen", bg="#ffe6f0")
        self.prize_label.pack(side="right", padx=20, pady=20)


        # Result Display
        self.result_label = tk.Label(self, text="", font=("Arial", 34, "bold"), bg="#ffe6f0")
        self.result_label.pack(pady=10)

    def get_random_questions(self, questions, num_questions):
        random.shuffle(questions)
        return questions[:num_questions]

    def start_quiz(self):
        """Initialize quiz and switch to main quiz interface."""
        self.score = 0
        self.current_question = 0
        self.coins = 0
        self.start_time = time.time()
        self.create_widgets()
        self.next_question()

        # Start background music on a loop
        pygame.mixer.music.load("gamemusic.mp3")
        pygame.mixer.music.play(-1)

        self.update_timer()

    def update_timer(self):
        """Update timer continuously."""
        elapsed_time = round(time.time() - self.start_time, 2)
        self.timer_label.config(text=f"Time: {elapsed_time}")
        self.after(100, self.update_timer)  # Update every 100ms





    def next_question(self):
        if self.current_question < len(self.questions_to_ask):
           question_data = self.questions_to_ask[self.current_question]
           self.question_label.config(text=f"Question {self.current_question + 1}: {question_data['question']}")
           for i, option in enumerate(question_data["options"]):
            self.option_buttons[i].config(text=option)
        else:
            self.end_quiz()


  
    

    def check_answer(self, selected_option=None):
        correct_answer = self.questions_to_ask[self.current_question]["answer"]

    # If selected_option is None, use the entry field as an answer
        if selected_option is None:
           selected_answer = self.answer_entry.get()
        else:
           selected_answer = self.option_buttons[selected_option].cget("text")

        if selected_answer == correct_answer:
            self.score += 1
            self.coins += 5000  # Increase coins for correct answers
            self.result_label.config(text="Correct!", fg="green")

            # Play cheering sound on a separate channel
            cheer_sound = pygame.mixer.Sound(CHEER_SOUND)
            cheer_channel = pygame.mixer.Channel(1)
            cheer_channel.play(cheer_sound)

            # Add sparkles effect
            self.show_sparkles()

            # Update the prize display
            self.prize_label.config(text=f"Coins: {self.coins}")

        else:
            self.result_label.config(text=f"Incorrect! The correct answer is: {correct_answer}", fg="red")
            self.after(1500, self.restart_quiz)

        self.current_question += 1
        self.after(1500, self.next_question)

    def show_sparkles(self):
        # Add animated sparkles effect
        for i in range(10):
            sparkle = tk.Label(self, text="✨", font=("Arial", 24), fg="silver")
            sparkle.place(x=random.randint(100, 700), y=random.randint(100, 500))
            self.after(300, sparkle.place_forget)

    def restart_quiz(self):
        self.answer_entry.delete(0, tk.END)
        self.next_question()

    def end_quiz(self):
        """Display results at the end of the quiz."""
        self.result_label.config(text=f"Quiz Over! Your score: {self.score}/{TOTAL_QUESTIONS}", fg="blue")
        self.submit_button.pack_forget()
        self.answer_entry.pack_forget()

        # Display final coins and give an option to restart or exit
        self.final_label = tk.Label(self, text=f"Coins Earned: {self.coins}", font=("Arial", 24, "bold"), bg="#ffe6f0")
        self.final_label.pack(pady=20)

        self.restart_button = tk.Button(self, text="Restart Quiz", font=("Arial", 24), command=self.restart_quiz)
        self.restart_button.pack(pady=10)

        self.quit_button = tk.Button(self, text="Exit", font=("Arial", 24), command=self.quit)
        self.quit_button.pack(pady=10)

if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()
