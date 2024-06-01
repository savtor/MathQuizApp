import tkinter as tk
import random

class MathQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x600")
        self.label = tk.Label(root, text="Hello", font=('Arial', 20))
        self.label.pack()
        
        self.frame = tk.Frame(root)
        self.frame.pack()
        
        self.name_label = tk.Label(self.frame, text="Enter your name: ")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(self.frame)
        self.name_entry.grid(row=0, column=1)
        self.start_button = tk.Button(self.frame, text="Start", command=self.start_quiz)
        self.start_button.grid(row=1, columnspan=2)

        self.level_label = tk.Label(root, text="Select Level: ")
        self.level_label.pack()
        
        self.level_var = tk.IntVar(value=1)
        for level in range(1, 5):
            tk.Radiobutton(root, text=f"Level {level}", variable=self.level_var, value=level).pack()
        
        self.quiz_frame = tk.Frame(root)
        self.quiz_frame.pack(pady=20)
        self.question_label = tk.Label(self.quiz_frame, text="", font=('Arial', 16))
        self.question_label.grid(row=0, column=0, columnspan=2)
        
        self.answer_entry = tk.Entry(self.quiz_frame)
        self.answer_entry.grid(row=1, column=0)
        self.answer_button = tk.Button(self.quiz_frame, text="Submit", command=self.check_answer)
        self.answer_button.grid(row=1, column=1)
        
        self.result_label = tk.Label(root, text="", font=('Arial', 14))
        self.result_label.pack(pady=10)
        
        self.score = 0
        self.attempts = 0
        self.current_question = ()
        self.name = ""

    def start_quiz(self):
        self.name = self.name_entry.get()
        self.level = self.level_var.get()
        self.score = 0
        self.attempts = 0
        self.result_label.config(text="")
        self.next_question()
    
    def next_question(self):
        self.current_question = self.generate_integer(self.level)
        num1, num2 = self.current_question
        self.question_label.config(text=f"{num1} + {num2} = ")
        self.answer_entry.delete(0, tk.END)
    
    def check_answer(self):
        try:
            answer = int(self.answer_entry.get())
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter a number.")
            return
        
        num1, num2 = self.current_question
        if answer == num1 + num2:
            self.score += 1
            self.result_label.config(text="Correct!")
        else:
            self.result_label.config(text=f"EEE. {num1} + {num2} = {num1 + num2}")
        
        self.attempts += 1
        if self.attempts < 10:
            self.next_question()
        else:
            self.result_label.config(text=f"Score: {self.score}. You are great. Thank you, {self.name}!")

    def generate_integer(self, level):
        ranges = {1: (0, 9), 2: (10, 99), 3: (100, 999), 4: (1000, 9999)}
        num1 = random.randint(*ranges[level])
        num2 = random.randint(*ranges[level])
        return num1, num2

if __name__ == "__main__":
    window = tk.Tk()
    app = MathQuizApp(window)
    window.mainloop()
